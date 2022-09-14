from django.urls import path
from app.organization.views import OrganizationModelViewSet,CityModelViewSet,TeacherModelViewSet
from rest_framework.routers import DefaultRouter

urlpatterns=[

]
router = DefaultRouter()
router.register(r'citys',CityModelViewSet)
router.register(r'organizations',OrganizationModelViewSet)
router.register(r'teachers',TeacherModelViewSet)
urlpatterns += router.urls