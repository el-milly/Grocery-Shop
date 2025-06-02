from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from authentication_app.models import user_profile


class User_Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = user_profile
        fields = ['user', 'first_name', 'last_name', 'avatar_img', 'email']