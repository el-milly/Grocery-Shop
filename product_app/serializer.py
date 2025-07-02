from rest_framework import serializers
from .models import CategoryModel, ProductModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = CategoryModel

    def create(self, validated_data):
        # Check if category with this name already exists
        if CategoryModel.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("A category with this name already exists.")
        
        # Create and return the new category
        return CategoryModel.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'category', 'slug', 'product_id']
        model = ProductModel
        extra_kwargs = {
            'slug': {'read_only': True}
        }
    def create(self, validated_data):
        if ProductModel.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("A product with this name already exists")
        return ProductModel.objects.create(**validated_data)