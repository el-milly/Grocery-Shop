from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CartSerializer
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return Response({'Response': 'use post method'})
    
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)