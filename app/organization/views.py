from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import City,Organization,Teacher
from .serializers import CitySerializers,TeacherSerializers,OrganizationSerializers
# Create your views here.
class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class OrganizationModelViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers