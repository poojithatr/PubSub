from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDetail

from .serializers import UserSerializer
from .models import UserDetail


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = UserDetail.objects.all().order_by('name')
#     serializer_class = UserSerializer

@api_view(['GET'])
def UserViewSet(request):
    usersData=UserSerializer(UserDetail.objects.all().order_by('name'), many=True)
    return Response(usersData.data)


@api_view(['POST'])
def UserCreate(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

