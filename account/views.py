from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import serializers
from .models import UserAccount
from .serializers import UserRegistrationSerializers

# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request):
       user_data = UserRegistrationSerializers(data=request.data) 

       if UserAccount.objects.filter(**request.data).exists():
           raise serializers.ValidationError('The date is already exist')
       user_data.is_valid(raise_exception=True)
       user = user_data.save()
       return Response({"message": "User registered successfully"})
    

class UserLoginView(APIView):
    def post(self, request):
        email =request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)