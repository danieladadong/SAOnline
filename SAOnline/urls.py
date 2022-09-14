"""SAOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import users.urls,course.urls,organization.urls,operation.urls,exam.urls
from users.views import LoginView,RegistView
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('api/user/',include(users.urls)),
    path('api/course/',include(course.urls)),
    path('api/organization/',include(organization.urls)),
    path('api/operation/',include(operation.urls)),
    path('api/login/',LoginView.as_view()),
    path('api/regist/',RegistView.as_view()),
    path('api/exam/',include(exam.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api-docs/', include_docs_urls(title='接口文档',description='这是一个接口文档的demo'))
]
