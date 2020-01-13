from .serializers import ApartmentSerializer, UserSerializer
from .models import Apartment, User
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.http import Http404,JsonResponse
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .mixins import MyPaginationMixin
import json
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



# Create your views here.


class API_Root(APIView):

    ''' List of all endpoints'''
    permission_classes = [AllowAny]
    def get(self,request, format=None):
        return Response({
            'users':reverse('UserList',request=request, format=format),
            'apartments':reverse('ApartmentList', request=request, format=format),
            'login':reverse('Login', request=request, format=format)
        })

class ApartmentList(APIView,MyPaginationMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ApartmentSerializer
    pagination_class = LimitOffsetPagination
    queryset = Apartment.objects.all()
    
   
    # def get(self,request):
    #     print(self.queryset)
    #     page = self.paginate_queryset(self.queryset)
    #     print(page)
    #     if page is not None:
    #         serializer = self.serializer_class(page, many=True)
    #         return self.get_paginated_response(serializer.data)
        
    
    def get(self,request):
        apartments = Apartment.objects.all()
        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data)
        
        
    def post(self, request, format=None):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



'''
class ApartmentList(GenericAPIView):
    pagination_class = LimitOffsetPagination
    apartments = Apartment.objects.all()

    def get(self, request):
        page = self.paginate_queryset(self.apartments)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ApartmentSerializer(self.apartments, many=True)
        return Response(serializer.data)
'''
class UserList(APIView, MyPaginationMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS  
    permission_classes = [AllowAny]

    '''
    Retrieves all instance user's instances

    '''

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            users = serializer.save()
            if users:
                token = Token.objects.create(user=users)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    phone_number = request.data.get("phone_number")
    if phone_number is None:
        return Response({'error': 'Please provide your phone number'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(phone_number=phone_number)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class UserDetails(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApartmentDetails(APIView):
    """
    Retrieve, update or delete an apartment instance.
    """
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Apartment.objects.get(pk=pk)
        except Apartment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ApartmentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ApartmentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)