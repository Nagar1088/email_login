from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =('id', 'email', 'name', 'password')
        extra_Kwargs = {'password': {'write_only': True}}



def create(self,validate_data):
    user=User.objects.create_user(
        email=validate_data['email'],
        name=validate_data['name'],
        passwoed=validate_data['password']
    )
    return user