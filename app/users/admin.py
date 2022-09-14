from django.contrib import admin

# Register your models here.
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileInfo(admin.ModelAdmin):
    list_display = ['id', 'nick_name', 'gender', 'birthday', 'address', 'mobile']
    list_display_links = ('nick_name',)
    list_filter = ('nick_name','mobile')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        id = User.objects.get(username=request.user).id
        return UserProfile.objects.filter(id=id) or qs.none()


admin.site.site_header = 'SAO在线学习系统后台'
admin.site.register(UserProfile, UserProfileInfo)
