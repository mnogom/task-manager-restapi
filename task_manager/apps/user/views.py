from .serializers import UserSerializer
from .models import User
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView)
from django.shortcuts import render  # noqa: F401


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
