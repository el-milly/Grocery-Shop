from rest_framework.views import APIView
from django.shortcuts import render
from kafka import KafkaProducer
from rest_framework.response import Response
from .models import ProductsModel
from .serializer import ProductsListSerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
import json
# Create your views here.
class ProductsListView(APIView):
    def get(self, request):
        return Response({'detail': 'Use post method instead of get'})
    def post(self, request):
        serializer = ProductsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProductsShowView(APIView):
    def get(self, request):
        products = ProductsModel.objects.all()
        serializer = ProductsListSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        return Response({'Detail': 'Use get method'})

class ProductUrlView(APIView):
    renderer_classes = JSONRenderer
    def get(self, request, slug):
        product = get_object_or_404(ProductsModel, slug=slug)
        serializer = ProductsListSerializer(product)
        return Response(serializer.data)
    def post(self, request):
        return Response({'detail': 'Use get method'})

class CartSendView(APIView):

    def get(self, request):
        return Response({'detail': 'use post method'})
    def post(self, request):
        serializer = ProductsListSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.data.get('user_id')
            self.start_kafka_producer(
                user_id=user_id,
                name=serializer.validated_data['name'],
                price=serializer.validated_data['price']
            )
            return Response({'user_id': user_id})
        return Response(serializer.errors)
    def start_kafka_producer(self, user_id, name, price):
        producer = KafkaProducer(
            bootstrap_servers='broker:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
                )
        producer.send('cart_events',{
            'event_type': 'item_added',
            'name': name,
            'user_id': user_id,
            'price': price,
        }
        )