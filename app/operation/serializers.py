from rest_framework import serializers
from app.operation.models import CourseComment,UserFavorite,UserMessage,Notice,ChatUserList
from app.users.models import UserProfile,User
from app.course.models import Course
from django.conf import settings

class CourseCommentSerializers(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    class Meta:
        fields = "__all__"
        model = CourseComment
    def get_users(self,obj):
        query_set = obj.user
        return [{"id":query_set.id,"name":query_set.nick_name,"image":"http://localhost:8000/media/"+str(query_set.image)}]

class UserFavoriteSerializers(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    class Meta:
        fields = "__all__"
        model = UserFavorite
    def get_users(self,obj):
        query_set = obj.user
        return [{"id":query_set.id,"name":query_set.nick_name}]


class UserMessageSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserMessage


class NoticeSerializers(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    users = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    class Meta:
        fields = "__all__"
        model = Notice
    def get_courses(self,obj):
        query_set = obj.course
        return [{"id":query_set.id,"name":query_set.name}]
    def get_users(self,obj):
        query_set = obj.user
        return [{"id":query_set.id,"name":query_set.nick_name}]


class ChatUserListSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ChatUserList