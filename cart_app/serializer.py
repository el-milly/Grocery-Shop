from rest_framework import serializers
from .models import CartModel
class CartSerializer(serializers.APIView):
    class Meta:
        fields = ["id", "user_id", "items", "created_at", "updated_at"]
        model = CartModel
    
    def validate_items(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("items must be a list")
        for item in items:
            if not all(key in item for key in ["product_id", "quantity"]):
                raise serializers.ValidationError("Each item must have product_id and quantity")

        return value