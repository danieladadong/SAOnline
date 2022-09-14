from django.contrib import admin

# Register your models here.
from .models import Organization, Teacher, City


class OrganizationInfo(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'tag', 'address', 'is_authentication']
    list_display_links = ('id','name', 'category', 'tag','address')
    list_filter = ('name','is_authentication')


class TeacherInfo(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'work_year', 'work_company', 'work_position']
    list_display_links = ('id', 'name',)
    list_filter = ('name','organization','work_position')


class CityInfo(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ('id', 'name')
    list_filter = ('name','id')


admin.site.register(Organization, OrganizationInfo)
admin.site.register(Teacher, TeacherInfo)
admin.site.register(City, CityInfo)
