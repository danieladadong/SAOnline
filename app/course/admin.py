from django.contrib import admin

# Register your models here.
from .models import Course,CourseResource,Lesson,Video,UserCourse,UserVideo,Schedule
from django.contrib.auth.models import User

class CourseInfo(admin.ModelAdmin):
    list_display = ['id','name','teacher_name','desc']
    list_display_links = ('id','name','teacher_name')
    list_filter = ('id','name','teacher')

    @admin.display(description='教师')
    def teacher_name(self,obj):
        return obj.teacher.name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        return Course.objects.filter(teacher=id) or qs.none

class LessonInfo(admin.ModelAdmin):
    list_display = ['id','course_name','name','add_time']
    list_display_links = ('id','name','course_name')
    list_filter = ('course',)
    ordering = ('course',)

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return Lesson.objects.filter(course__in=courses) or qs.none

class VideoInfo(admin.ModelAdmin):
    list_display = ['course_name','lesson_name','name','url','learn_times','add_time']
    list_display_links = ('name','course_name','lesson_name')
    list_filter = ('course','lesson','name')

    @admin.display(description='章节')
    def lesson_name(self,obj):
        return obj.lesson.name

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        lessons = Lesson.objects.filter(course__in=courses)
        return Video.objects.filter(lesson__in=lessons) or qs.none

class CourseResourceInfo(admin.ModelAdmin):
    list_display = ['id','course_name','name','resource','add_time']
    list_display_links = ('name','course_name')
    list_filter = ('course','name')

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return CourseResource.objects.filter(course__in=courses) or qs.none

class UserCourseInfo(admin.ModelAdmin):
    list_display = ['id','course_name','user_name','add_time']
    list_display_links = ('course_name',)
    list_filter = ('course','user')

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name

    @admin.display(description='用户')
    def user_name(self,obj):
        return obj.user.nick_name

class UserVideoInfo(admin.ModelAdmin):
    list_display = ['id','video_name','course_name','user_name','learned_time','is_finish']
    list_display_links = ('video_name','course_name','user_name')
    list_filter = ('course','user','video')

    @admin.display(description='视频')
    def video_name(self,obj):
        return obj.video.name

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name

    @admin.display(description='用户')
    def user_name(self,obj):
        return obj.user.nick_name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = UserVideo.objects.get(username=request.user).id
        return UserVideo.objects.filter(id=id) or qs.none()

class ScheduleInfo(admin.ModelAdmin):
    list_display = ['id','label','user']
    list_display_links = ('label','user')
    list_filter = ('user',)

admin.site.register(Course,CourseInfo)
admin.site.register(CourseResource,CourseResourceInfo)
admin.site.register(Lesson,LessonInfo)
admin.site.register(Video,VideoInfo)
admin.site.register(UserCourse,UserCourseInfo)
admin.site.register(UserVideo,UserVideoInfo)
admin.site.register(Schedule,ScheduleInfo)

