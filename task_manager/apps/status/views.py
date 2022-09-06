"""Views."""

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Status
from .serializers import StatusSerializer


class ListCreateStatusView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Status.objects.order_by('created_at')
    serializer_class = StatusSerializer


class RetrieveUpdateDestroyStatusView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
