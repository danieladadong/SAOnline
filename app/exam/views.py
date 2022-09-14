from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from app.exam.serializers import ExamPaperSerializer,QuestionBankSerializer,RecordSerializer
from exam.models import ExamPaper,QuestionBank,Record
from django.views.generic.base import View
import json
import datetime

# Create your views here.
class ExamPaperModelViewSet(ModelViewSet):
    queryset = ExamPaper.objects.all()
    serializer_class = ExamPaperSerializer
    filter_fields = ('course_id',)

class QuestionBankModelViewSet(ModelViewSet):
    queryset = QuestionBank.objects.all()
    serializer_class = QuestionBankSerializer
    filter_fields = ('course_id',)

class RecordModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_fields = ('user_id',)

class calculateGrade(View):
    def get(self,request):
        pass
    def post(self,request):
        json_data = json.loads(request.body.decode())
        epid = json_data['id']
        course = json_data['course']
        questions = json_data['pid']
        user = json_data['user']
        scores = 0
        for key,value in questions.items():
            QB = QuestionBank.objects.get(id=key)
            if value == QB.answer:
                scores += QB.score
        Record.objects.create(grade = scores,rtime=datetime.datetime.now(),course_id=course,user_id=user,exampaper_id=epid)
        return HttpResponse(scores)
