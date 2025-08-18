from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from .models import ProductsModel
from .serializer import ProductsListSerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
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