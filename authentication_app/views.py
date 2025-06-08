from rest_framework.response import Response
from .serializer import UserProfileSerializer, UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from knox.models import AuthToken


# Create your views here.

class UserViewApi(APIView):
    def get(self, request):
        return Response({'message': 'Use post'})

    def post(self,request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            profile = serializer.save()
            user = profile.user
            token = AuthToken.objects.create(user)[1]
            
            return Response({"profile": UserProfileSerializer(profile).data, "token": token})        
        return Response(serializer.errors)


class UserLoginView(APIView):
    def get(self, request):
        return Response({"message": "Use post"})
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'})
        
        token = AuthToken.objects.get_or_create(user)[1]
        
        return Response({"user_data": UserSerializer(user).data, "token": token})
    
class CheckView(APIView):
    def get(self,request):
        if not request.user.is_autenticated:
            return Response({"detail": "Please, authentication!"})
        user = request.user
        token = AuthToken.objects.get(user=request.user)
        return Response({"username": user.username,
                         "email": "user.email",
                         "token": token})
    def post(self, request):
        return Response({"detail": "Please, use a get method"})

        








