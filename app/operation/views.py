from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.operation.models import CourseComment, UserFavorite, UserMessage, Notice,ChatUserList
from app.operation.serializers import CourseCommentSerializers, UserFavoriteSerializers, UserMessageSerializers, \
    NoticeSerializers,ChatUserListSerializers
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CourseCommentModelViewSet(ModelViewSet):
    queryset = CourseComment.objects.all()
    serializer_class = CourseCommentSerializers
    filter_fields = ('course_id',)


class UserFavoriteModelViewSet(ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializers
    filter_fields = ('user_id', 'fav_type', 'fav_id')


class UserMessageModelViewSet(ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializers
    filter_fields = ('user',)


class NoticePage(PageNumberPagination):
    page_size_query_param = "size",
    page_query_param = "page"

class NoticeModelViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers
    filter_fields = ('user_id', 'course_id')
    pagination_class = NoticePage

# def chat(request, room_name):
#     return render(request, 'index.html', {
#         'room_name': room_name})


class ChatUserListModelViewSet(ModelViewSet):
    queryset = ChatUserList.objects.all()
    serializer_class = ChatUserListSerializers
    filter_fields = ('user','touser')
