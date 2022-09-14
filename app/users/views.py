import json

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserProfileSerializers,UserSerializers
from app.users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from app.course.models import Schedule


# Create your views here.
class LoginView(View):
    def get(self, request):
        pass

    @csrf_exempt
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                data = {
                    "status": 200,
                    "success": True,
                    "message": "登录成功！",
                    "mobile": username
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {
                    "status":400,
                    "success": False,
                    "message": "用户名或密码错误！"
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data = {
                "status": 400,
                "success": False,
                "message": "用户不存在，请先注册！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class RegistView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        same_user = User.objects.filter(username=username)
        if same_user:
            data = {
                "status":400,
                "success": False,
                "message": "账号已存在！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                            first_name=first_name)
            user.save()
            profile = UserProfile.objects.create(id=user.id, nick_name=first_name + last_name, mobile=user.username)
            profile.save()
            for i in range(5):
                schedule = Schedule.objects.create(label="周"+str(i+1),user_id=user.id)
                schedule.save()
            data = {
                "status": 200,
                "success": True,
                "message": "创建成功！"
            }
            return HttpResponse(json.dumps(data), content_type='application/json')


class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    filter_fields = ('mobile',)

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_fields = ('id',)

