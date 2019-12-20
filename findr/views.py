from .serializers import ApartmentSerializer, UserSerializer
from .models import Apartment, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from django.http import Http404
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings



# Create your views here.
class MyPaginationMixin(object):

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination 
        is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(
            queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given 
        output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

'''
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('UserList', request=request, format=format),
        'apartments': reverse('ApartmentList', request=request, format=format)

    })
'''


class API_Root(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, format=None):
        return Response({
            'users':reverse('UserList',request=request, format=format),
            'apartments':reverse('ApartmentList', request=request, format=format)
        })

class ApartmentList(APIView,MyPaginationMixin):
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    apartments = Apartment.objects.all()
    serializer = ApartmentSerializer

    def get(self,request):
        
        page = self.paginate_queryset(self.apartments)
        if page is not None:
            serializer = self.serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApartmentDetails(APIView):
    """
    Retrieve, update or delete an apartment instance.
    """
  
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
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


class UserList(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            users = serializer.save()
            if users:
                token = Token.objects.create(users=users)
                json = serializer.data
                json['token'] = token.key
                return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

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



