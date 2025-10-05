from rest_framework import serializers
from .models import CartModel
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["user_id","items", "created_at", "updated_at"]
        model = CartModel
        def create(self, validated_data):
            print("Validated data:", validated_data)  
            return super().create(validated_data)