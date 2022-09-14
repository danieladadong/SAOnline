from rest_framework import serializers
from app.course.models import Course, Lesson, Video, CourseResource, UserCourse, UserVideo, Schedule
from app.organization.models import Teacher, Organization
from app.users.models import UserProfile



class CourseSerializers(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    teachers = serializers.SerializerMethodField()
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

    class Meta:
        fields = "__all__"
        model = Course

    def get_organizations(self, obj):
        query_set = obj.organization
        return [{"id": query_set.id, "name": query_set.name}]

    def get_teachers(self, obj):
        query_set = obj.teacher
        return [{'id': query_set.id, 'name': query_set.name}]




class VideoSerializers(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        fields = "__all__"
        model = Video


class LessonSerializers(serializers.ModelSerializer):
    # courses = serializers.SerializerMethodField()
    # course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    videos = VideoSerializers(many=True)
    class Meta:
        fields = "__all__"
        model = Lesson
    # def get_courses(self, obj):
    #     query_set = obj.course
    #     return [{"id": query_set.id, "name": query_set.name}]


class CourseResourceSerializers(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        fields = "__all__"
        model = CourseResource

    def get_courses(self, obj):
        query_set = obj.course
        return [{"id": query_set.id, "name": query_set.name}]


class UserCourseSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserCourse


class UserVideoSerializers(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    video = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all())
    lessons = serializers.SerializerMethodField()
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())
    courses = serializers.SerializerMethodField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    users = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        fields = "__all__"
        model = UserVideo

    def get_courses(self, obj):
        query_set = obj.course
        return [{"id": query_set.id, "name": query_set.name}]

    def get_users(self, obj):
        query_set = obj.user
        return [{"id": query_set.id, "name": query_set.nick_name}]

    def get_lessons(self, obj):
        query_set = obj.lesson
        return [{"id": query_set.id, "name": query_set.name}]

    def get_videos(self, obj):
        query_set = obj.video
        return [{"id": query_set.id}]


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Schedule
