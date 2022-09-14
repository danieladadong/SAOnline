from django.urls import path
from .views import CourseModelViewSet,LessonModelViewSet,\
    VideoModelViewSet,CourseResourceModelViewSet,\
    UserCourseModelViewSet,UserVideoModelViewSet,\
    ScheduleModelViewSet,getbanner,LearningEarlyWarning
from rest_framework.routers import DefaultRouter
from .views import stream_video

urlpatterns=[
    path('stream_video/', stream_video),
    path('getbanner/',getbanner.as_view()),
    path('learning/',LearningEarlyWarning.as_view())
]
router = DefaultRouter()
router.register(r'courses',CourseModelViewSet)
router.register(r'lessons',LessonModelViewSet)
router.register(r'videos',VideoModelViewSet)
router.register(r'c_resources',CourseResourceModelViewSet)
router.register(r'u_courses',UserCourseModelViewSet)
router.register(r'u_videos',UserVideoModelViewSet)
router.register(r'schedule',ScheduleModelViewSet)
urlpatterns += router.urls