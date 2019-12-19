from rest_framework import serializers
from .models import User,Apartment
from rest_framework.validators import UniqueValidator
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    phone_number = serializers.CharField(required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    def create(self,validated_data):
        user = User.objects.create(validated_data['username'], validated_data['phone_number'])
        return user

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