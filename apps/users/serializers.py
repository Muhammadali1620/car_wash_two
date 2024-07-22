from django.core.exceptions import ValidationError

from rest_framework import serializers

from django.contrib.auth import get_user_model

from apps.users.models import CustomUser

class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('role', 'username', 'car_wash', 'password')

    def validate(self, attrs):
        role  = attrs.get('role', '')
        if role == '':
            attrs['role'] = CustomUser.Role.DEV.value
        if attrs['role'] == CustomUser.Role.WASHER.value and not attrs['car_wash']:
            raise ValidationError({'car_wash': 'This field is required'})
        return attrs
    
    def validate(self, attrs):
        return super().validate(attrs)

class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'groups', 'user_permissions', 'last_login', 'date_joined')


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('groups', 'user_permissions', 'last_login', 'date_joined')
