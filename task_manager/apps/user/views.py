from .serializers import UserSerializer
from .models import User
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render  # noqa: F401


class UserList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
