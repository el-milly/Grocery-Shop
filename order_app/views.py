from order_project.serializer import OrderSerializer
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.


class OrderCreateView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"detail": "Use Post!"})
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data, context ={'request': request})
        if serializer.is_valid:
            serializer.save
            return Response({serializer.data})

        return Response({"detail": serializer.errors})