from django.contrib import admin

# Register your models here.
from .models import CourseComment,UserFavorite,UserMessage,Notice
from app.course.models import Course
from django.contrib.auth.models import User

class CourseCommentInfo(admin.ModelAdmin):
    list_display = ['id','course_name','user_name','add_time']
    list_display_links = ('course_name','user_name')
    list_filter = ('course','user')

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name

    @admin.display(description='用户')
    def user_name(self,obj):
        return obj.user.nick_name

class UserFavoriteInfo(admin.ModelAdmin):
    list_display = ['id','user_name','fav_id','fav_type','add_time']
    list_display_links = ('user_name',)
    list_filter = ('user','fav_type')

    @admin.display(description='用户')
    def user_name(self,obj):
        return obj.user.nick_name

class UserMessageInfo(admin.ModelAdmin):
    list_display = ['id','message','add_time']
    list_display_links = ('message',)

class NoticeInfo(admin.ModelAdmin):
    list_display = ['id','course_name','title','content','user_name','add_time']
    list_display_links = ('course_name','title','content')
    list_filter = ('course','title','user')

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
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return Notice.objects.filter(course__in=courses) or qs.none()

admin.site.register(CourseComment,CourseCommentInfo)
admin.site.register(UserFavorite,UserFavoriteInfo)
admin.site.register(UserMessage,UserMessageInfo)
admin.site.register(Notice,NoticeInfo)