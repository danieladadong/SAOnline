from django.urls import path
from rest_framework.routers import DefaultRouter
from app.exam.views import ExamPaperModelViewSet,QuestionBankModelViewSet,RecordModelViewSet,calculateGrade
urlpatterns=[
    path('calculate/',calculateGrade.as_view()),
]
router = DefaultRouter()
router.register(r'exampapers',ExamPaperModelViewSet)
router.register(r'questions',QuestionBankModelViewSet)
router.register(r'records',RecordModelViewSet)
urlpatterns += router.urls