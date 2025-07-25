from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CartSerializer
from rest_framework.response import Response
# Create your views here.


class CartView(APIView):
    def get(request):
        return Response({'Response': 'use post method'})
    
    def post(request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()