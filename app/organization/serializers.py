
from rest_framework import serializers
from app.organization.models import Organization,City,Teacher


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = City

class OrganizationSerializers(serializers.ModelSerializer):
    citys = serializers.SerializerMethodField()
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    class Meta:
        fields = "__all__"
        model = Organization
    def get_citys(self,obj):
        query_set = obj.city
        return [{"id":query_set.id,"name":query_set.name}]


class TeacherSerializers(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    class Meta:
        fields = "__all__"
        model = Teacher
    def get_organizations(self,obj):
        query_set = obj.organization
        return [{"id":query_set.id,"name":query_set.name}]