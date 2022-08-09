from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from django.shortcuts import render  # noqa: F401


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer