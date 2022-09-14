from django.urls import path
from app.operation.views import CourseCommentModelViewSet,UserFavoriteModelViewSet,UserMessageModelViewSet,\
    NoticeModelViewSet,ChatUserListModelViewSet
from rest_framework.routers import DefaultRouter
# from app.operation.views import chat

urlpatterns=[
    # path('chat/<str:room_name>/',chat)
]
router = DefaultRouter()
router.register(r'comments',CourseCommentModelViewSet)
router.register(r'favorites',UserFavoriteModelViewSet)
router.register(r'messages',UserMessageModelViewSet)
router.register(r'notices',NoticeModelViewSet)
router.register(r'chatuserlist',ChatUserListModelViewSet)
urlpatterns += router.urls