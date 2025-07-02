from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CategorySerializer, ProductSerializer
# Create your views here.


class CategoryView(APIView):
    def get(self, request):
        return Response({"detail": "Use post method instead of get method"})
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class ProductView(APIView):
    def get(self, request):
        return Response({"detail": "Use post method instead of get method"})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)