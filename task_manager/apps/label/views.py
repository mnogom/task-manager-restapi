"""Views."""

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Label
from .serializers import LabelSerializer


class ListCreateLabelView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Label.objects.order_by('created_at')
    serializer_class = LabelSerializer


class RetrieveUpdateDestroyLabelView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
