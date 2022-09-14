app_name = 'users'
from django.urls import path
from .views import UserProfileModelViewSet,UserModelViewSet
from rest_framework.routers import DefaultRouter
urlpatterns=[
]
router = DefaultRouter()
router.register(r'profiles',UserProfileModelViewSet)
router.register(r'user',UserModelViewSet)
urlpatterns += router.urls