from rest_framework_simplejwt.tokens import RefreshToken
from djoser.serializers import UserCreateSerializer,User
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','phone')
        






