from rest_framework import serializers
from .models import user_profile
from django.contrib.auth.models import User
from kafka import KafkaProducer
import json
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id','username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = user_profile
        fields = ['id','first_name', 'email', 'user', 'last_name']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password']
        )
        profile = user_profile.objects.create(user=user, **validated_data)
        
        producer = KafkaProducer(
            bootstrap_servers='broker:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send(
            'user-events',
            value={
                'event_type': 'user_created',
                'user_id': user.id,
            }
        )
        producer.flush()


        return profile