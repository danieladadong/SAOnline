from rest_framework import serializers
from exam.models import ExamPaper,QuestionBank,Record
from app.course.models import Course
from app.users.models import UserProfile
class QuestionBankSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        exclude = ('answer','difficulty')
        model = QuestionBank
    def get_courses(self,obj):
        query_set = obj.course
        return [{"id":query_set.id,"name":query_set.name}]

class ExamPaperSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    pid = QuestionBankSerializer(many=True)
    class Meta:
        fields = "__all__"
        model = ExamPaper
    def get_courses(self,obj):
        query_set = obj.course
        return [{"id":query_set.id,"name":query_set.name}]

class RecordSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    exampapers = serializers.SerializerMethodField()
    exampaper = serializers.PrimaryKeyRelatedField(queryset=ExamPaper.objects.all())
    class Meta:
        fields = "__all__"
        model = Record
    def get_users(self,obj):
        query_set = obj.user
        return [{"id":query_set.id,"name":query_set.nick_name}]
    def get_exampapers(self,obj):
        query_set = obj.exampaper
        return [{"id":query_set.id,"title":query_set.title}]