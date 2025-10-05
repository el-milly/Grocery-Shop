from rest_framework import serializers
from .models import ProductsModel
from kafka import KafkaProducer
class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug', 'category', 'price']
        model = ProductsModel

    def create(self, validated_data):
        if ProductsModel.objects.filter(name=validated_data['name']).exists():
            raise serializer.ValidationError('A product with the same name exists')
        return ProductsModel.objects.create(**validated_data)