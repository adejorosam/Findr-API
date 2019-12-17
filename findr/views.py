from django.shortcuts import render
from .serializers import ApartmentSerializer,UserSerializer
from .models import Apartment,User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.

class ApartmentList(APIView):

    def get(self,request):
        #pagination_class = BasicPagination
        queryset = Apartment.objects.all()
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(queryset,request)
        serializer = ApartmentSerializer(result_page,many=True, context={'request':request})
        return Response(serializer.data)

    def post(self):
        pass

class UserList(APIView):

    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self):
        pass





