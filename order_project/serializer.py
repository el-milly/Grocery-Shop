from order_app.models import OrderModel, ProductModel, CategoryModel
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id','name']
  
    def create(self, validated_data):
        if CategoryModel.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError
        
        instance = CategoryModel.objects.create(**validated_data)

        return instance
    

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = ProductModel
        fields = ['id','name', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        
        category, created = CategoryModel.objects.get_or_create(
            name=category_data['name'],
            defaults=category_data
        )
        
        product = ProductModel.objects.create(
            category=category,
            **validated_data
        )
        
        return product
class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderModel
        fields = ['contact_bio','address', 'date_of_order', 'count', 'product']
        extra_kwargs = {'address': {'write_only': True}}

    def create(self, validated_data):
        user = self.context['request'].user
        order_data = OrderModel.objects.create(user=user,**validated_data)
        return order_data