import json
import math
from collections import defaultdict
from operator import itemgetter
from django.db.models import Sum,Avg,Count
import django_filters
from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import CourseSerializers, LessonSerializers, \
    VideoSerializers, CourseResourceSerializers, \
    UserCourseSerializers, UserVideoSerializers, ScheduleSerializers
from app.course.models import Course, Lesson, Video, CourseResource, UserCourse, UserVideo, Schedule
from django.http import StreamingHttpResponse
import re, os
import mimetypes
from SAOnline import settings
from wsgiref.util import FileWrapper
from django_filters import rest_framework as filters
from django.views.generic.base import View
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class CourseFilter(django_filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr="icontains")
    teacher_id = filters.NumberFilter(field_name='teacher_id', lookup_expr="exact")
    tag = filters.CharFilter(field_name='tag', lookup_expr="icontains")
    category = filters.CharFilter(field_name='category', lookup_expr="icontains")
    organization = filters.NumberFilter(field_name='organization', lookup_expr="exact")
    is_publish = filters.BooleanFilter(field_name='is_publish',lookup_expr="exact")


class CoursePage(PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filterset_class = CourseFilter
    pagination_class = CoursePage


class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
    filter_fields = ('course_id',)


class VideoModelViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    filter_fields = ('lesson_id',)


class CourseResourcePage(PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"


class CourseResourceModelViewSet(ModelViewSet):
    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializers
    filter_fields = ('course_id', 'isVideo')
    pagination_class = CourseResourcePage


class UserCoursePage(PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"


class UserCourseModelViewSet(ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializers
    filter_fields = ('user_id', 'course')
    pagination_class = UserCoursePage


class UserVideoModelViewSet(ModelViewSet):
    queryset = UserVideo.objects.all()
    serializer_class = UserVideoSerializers
    filter_fields = ('course_id', 'video_id', 'user_id')


class SchedulePage(PageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"


class ScheduleModelViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers
    filter_fields = ('user_id', 'label')
    pagination_class = SchedulePage


def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not data: break
            if remaining: remaining -= len(data)
            yield data


def stream_video(request):
    path = "media/" + request.GET.get("path")  # 此为我的视频路径
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
    range_match = range_re.match(range_header)
    size = os.path.getsize(path)
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        if first_byte:
            first_byte = int(first_byte)
        else:
            first_byte = 0
        last_byte = first_byte + 1024 * 1024 * 8  # 8M per piece, the maximum volume of the response body
        if last_byte > size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(file_iterator(path, offset=first_byte, length=length), status=206,
                                     content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        # When the video stream is not obtained, the entire file is returned in the generator mode to save memory.
        resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


class UserCF(object):
    """ User based Collaborative Filtering Algorithm Implementation"""

    def __init__(self, trainData, similarity="cosine"):
        self._trainData = trainData
        self._similarity = similarity
        self._userSimMatrix = dict()  # 用户相似度矩阵

    def similarity(self):
        # 建立User-Item倒排表
        item_user = dict()
        for user, items in self._trainData.items():
            for item in items:
                item_user.setdefault(item, set())
                item_user[item].add(user)

        # 建立用户物品交集矩阵W, 其中C[u][v]代表的含义是用户u和用户v之间共同喜欢的物品数
        for item, users in item_user.items():
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    self._userSimMatrix.setdefault(u, defaultdict(int))
                    if self._similarity == "cosine":
                        self._userSimMatrix[u][v] += 1  # 将用户u和用户v共同喜欢的物品数量加一
                    elif self._similarity == "iif":
                        self._userSimMatrix[u][v] += 1. / math.log(1 + len(users))

        # 建立用户相似度矩阵
        for u, related_user in self._userSimMatrix.items():
            # 相似度公式为 |N[u]∩N[v]|/sqrt(N[u]||N[v])
            for v, cuv in related_user.items():
                nu = len(self._trainData[u])
                nv = len(self._trainData[v])
                self._userSimMatrix[u][v] = cuv / math.sqrt(nu * nv)

    def recommend(self, user, N, K):
        """
        用户u对物品i的感兴趣程度：
            p(u,i) = ∑WuvRvi
            其中Wuv代表的是u和v之间的相似度， Rvi代表的是用户v对物品i的感兴趣程度，因为采用单一行为的隐反馈数据，所以Rvi=1。
            所以这个表达式的含义是，要计算用户u对物品i的感兴趣程度，则要找到与用户u最相似的K个用户，对于这k个用户喜欢的物品且用户u
            没有反馈的物品，都累加用户u与用户v之间的相似度。
        :param user: 被推荐的用户user
        :param N: 推荐的商品个数
        :param K: 查找的最相似的用户个数
        :return: 按照user对推荐物品的感兴趣程度排序的N个商品
        """
        recommends = dict()
        # 先获取user具有正反馈的item数组
        if not self._trainData.__contains__(user):
            return None
        related_items = self._trainData[user]
        # 将其他用户与user按照相似度逆序排序之后取前K个
        for v, sim in sorted(self._userSimMatrix[user].items(), key=itemgetter(1), reverse=True)[:K]:
            # 从与user相似的用户的喜爱列表中寻找可能的物品进行推荐
            for item in self._trainData[v]:
                # 如果与user相似的用户喜爱的物品与user喜欢的物品重复了，直接跳过
                if item in related_items:
                    continue
                recommends.setdefault(item, 0.)
                recommends[item] += sim
        # 根据被推荐物品的相似度逆序排列，然后推荐前N个物品给到用户
        return dict(sorted(recommends.items(), key=itemgetter(1), reverse=True)[:N])

    def train(self):
        self.similarity()


class getbanner(View):
    def loadData(self):
        ucourses = UserCourse.objects.order_by('user_id')
        course_list = list()
        for item in ucourses:
            tmp = [item.user_id, item.course_id]
            course_list.append(tmp)
        trainData = dict()
        for user, item in course_list:
            trainData.setdefault(user, set())
            trainData[user].add(item)
        return trainData

    def post(self, request):
        userId = int(request.POST.get('uuid'))
        dataDict = self.loadData()
        usercf = UserCF(dataDict)
        usercf.train()
        CourseDict = UserCF.recommend(usercf, userId, 4, 50)
        if CourseDict is None or CourseDict.__len__() == 0:
            rest = json.dumps(list(), ensure_ascii=False)
            return HttpResponse(rest)
        courseIds = list(CourseDict.keys())
        courses = Course.objects.filter(id__in=courseIds)
        serializer = CourseSerializers(instance=courses, many=True, context={'request': request})
        rest = json.dumps(serializer.data, ensure_ascii=False)
        return HttpResponse(rest)

    def get(self, request):
        pass


class LearningEarlyWarning(View):

    def post(self, request):
        global courseVideo
        global userVideos
        global allUserVideos
        global userprogress
        global alluserprogress
        global progress
        userId = int(request.POST.get('uuid'))
        courseId = int(request.POST.get('course'))
        if list(Video.objects.values('course').annotate(learntime=Sum('learn_times')).filter(course=courseId)):
            courseVideo = list(Video.objects.values('course').annotate(learntime=Sum('learn_times')).filter(course=courseId))[0]['learntime']
        else:
            courseVideo=0
        if list(UserVideo.objects.values('course').annotate(learnedtime=Sum('learned_time')).filter(user=userId).filter(course=courseId)):
            userVideos = list(UserVideo.objects.values('course').annotate(learnedtime=Sum('learned_time')).filter(
            user=userId).filter(course=courseId))[0]['learnedtime']
        else:
            userVideos=0
        usertotal = list(UserCourse.objects.values('course').annotate(total=Count('id')).filter(course=courseId))[0]['total']
        if list(UserVideo.objects.values('course').annotate(alllearnedtime=Sum('learned_time')).filter(course=courseId)):
            allUserVideos = list(UserVideo.objects.values('course').annotate(alllearnedtime=Sum('learned_time')).filter(course=courseId))[0]['alllearnedtime']
        else:
            alluserprogress=0
        userprogress = userVideos / courseVideo
        alluserprogress = (allUserVideos / usertotal) / courseVideo
        progress = userprogress / alluserprogress
        if userprogress is not 0 and progress is not 0:
            if userprogress < 0.8 or progress < 0.8:
                data = {
                    "status": 200,
                    "success": True,
                    "message": "您的进度远远落后于其他同学！请注意！"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {
                    "status": 200,
                    "success": True,
                    "message": "您的进度正常请保持现在的状态！"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                "status": 200,
                "success": True,
                "message": "您还未参加学习！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
    def get(self, request):
        pass
