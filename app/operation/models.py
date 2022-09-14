import datetime

from django.db import models
from app.course.models import Course
from app.users.models import UserProfile
from django.contrib.auth.models import User
from app.organization.models import Teacher
# Create your models here.
class CourseComment(models.Model):
    course = models.ForeignKey(Course, verbose_name="评论课程", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name="评论用户", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="评论内容", max_length=255)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "coursecomment"
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name



class UserFavorite(models.Model):
    TYPE_CHOICES = (
        (1, '机构'),
        (2, '课程'),
        (3, '教师'),
    )
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name="收藏用户ID", default=0)
    fav_type = models.IntegerField(verbose_name="收藏类型", choices=TYPE_CHOICES, default=1)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "userfavorite"
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # 为0则发送给所有用户，否则就是用户的id
    user = models.IntegerField(verbose_name="用户", default=0)
    message = models.CharField(verbose_name="消息内容", max_length=255)
    has_read = models.BooleanField(verbose_name="是否已读", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "usermessage"
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class Notice(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程",on_delete=models.CASCADE)
    title = models.CharField(verbose_name="标题",max_length=30,default="")
    content = models.TextField(verbose_name="内容")
    user = models.ForeignKey(UserProfile,verbose_name="发布用户",on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())
    class Meta:
        db_table = "notice"
        verbose_name = "课程公告"
        verbose_name_plural = verbose_name

class ChatUserList(models.Model):
    user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)
    touser = models.IntegerField(verbose_name="聊天用户",default=0)
    username = models.CharField(verbose_name="用户名",max_length=30,default="")

    class Meta:
        db_table = "chatuserlist"
        verbose_name = "聊天用户列表"
        verbose_name_plural = verbose_name



