from rest_framework import serializers
from .models import User,Apartment
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
'''
class ApartmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentCategory
        fields = '__all__'
'''