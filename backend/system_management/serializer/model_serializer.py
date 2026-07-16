from rest_framework import serializers

from system_management.models import (
    Role,
    Race,
    Title,
    Gender,
    Province
)

class ViewRoleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class ViewRaceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = '__all__'


class ViewTitleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class ViewGenderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class ViewProvinceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'

