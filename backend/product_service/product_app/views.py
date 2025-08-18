from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CategoryModel, ProductModel
from .serializer import CategorySerializer, ProductSerializer
# Create your views here.


class CategoryView(APIView):
    def get(self, request):
        return Response({"detail": 'Use post'})
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CategoryViewGet(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'detail': serializer.data})
    def post(self, request):

        return Response({'detail': 'Use get request'})


class ProductView(APIView):
    def get(self, request):
        return Response({"detail": "Use post method instead of get method"})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProductViewGet(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'detail': serializer.data})
    def post(self, request):
        return Response({'detail': 'use get request'})