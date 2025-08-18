from rest_framework import serializers
from .models import CategoryModel, ProductModel
from kafka import KafkaProducer
import json
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name', 'slug']
        model = CategoryModel
        extra_kwargs = {
            'slug': {'read_only': True}
        }

    def create(self, validated_data):
        # Check if category with this name already exists
        if CategoryModel.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("A category with this name already exists.")
        
        # Create and return the new category
        return CategoryModel.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'category', 'slug', 'product_id', 'price', 'description', 'protein', 'carbs', 'fats', 'kcal']
        model = ProductModel
        extra_kwargs = {
            'slug': {'read_only': True}
        }
    def create(self, validated_data):
        if ProductModel.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("A product with this name already exists")
        product = ProductModel.objects.create(**validated_data)
        producer = KafkaProducer(bootstrap_servers='broker:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
       
        producer.send('created-product', value={
            'event-type': 'created-product',
            'name': product.name,
            'category': product.category.name,
            'slug': product.slug,
            'product_id': product.product_id,
            'price': product.price,
            'description': product.description,
            'protein': product.protein,
            'fats': product.fats,
            'carbs': product.carbs,
            'kcal': product.kcal,
        })
        producer.flush()
        return product