from django.contrib import admin

# Register your models here.
from .models import QuestionBank,ExamPaper,Record
from app.course.models import Course
from django.contrib.auth.models import User

class ExamPaperInfo(admin.ModelAdmin):
    list_display = ['id','course_name','title','time','examtime']
    list_display_links = ('course_name','title')
    list_filter = ('course','title')

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return ExamPaper.objects.filter(course__in=courses) or qs.none()

class QuestionBankInfo(admin.ModelAdmin):
    list_display = ['id','course_name','title','qtype','score']
    list_display_links = ('course_name','title')
    list_filter = ('course','title')

    @admin.display(description='课程')
    def course_name(self, obj):
        return obj.course.name
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return QuestionBank.objects.filter(course__in=courses) or qs.none()

class RecordInfo(admin.ModelAdmin):
    list_display = ['id','user_name','course_name','exampaper_name','grade','rtime']
    list_display_links = ('user_name','course_name','exampaper_name')
    list_filter = ('user','course','exampaper')

    @admin.display(description='用户')
    def user_name(self,obj):
        return obj.user.nick_name

    @admin.display(description='课程')
    def course_name(self,obj):
        return obj.course.name

    @admin.display(description='试卷')
    def exampaper_name(self,obj):
        return obj.exampaper.title

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        courses = Course.objects.filter(teacher=id) or qs.none
        return Record.objects.filter(course__in=courses) or qs.none()

admin.site.register(QuestionBank,QuestionBankInfo)
admin.site.register(ExamPaper,ExamPaperInfo)
admin.site.register(Record,RecordInfo)