from django.shortcuts import render
from .serializers import HouseSerializer,UserSerializer
from .models import House,User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class HouseList(APIView):

    def get(self,request):
        queryset = House.objects.all()
        serializer = HouseSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class CustomUserList(APIView):

    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self):
        pass






