from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request,*args,**kwargs):
    return Response(data="Welcome To Home",status=status.HTTP_200_OK)