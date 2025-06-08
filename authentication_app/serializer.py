from rest_framework import serializers
from .models import user_profile
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = user_profile
        fields = ['first_name', 'email', 'user', 'last_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password']
        )
        profile = user_profile.objects.create(user=user, **validated_data)
        return profile