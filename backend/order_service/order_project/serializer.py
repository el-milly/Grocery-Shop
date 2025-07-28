from order_app.models import OrderModel, ProductModel, CategoryModel
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['contact_bio','address', 'date_of_order', 'count', 'product_id']
        extra_kwargs = {'address': {'write_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        order_data = OrderModel.objects.create(user=user,**validated_data)
        return order_data