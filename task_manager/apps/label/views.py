"""Views."""

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Label
from .serializers import LabelSerializer


class ListCreateLabelView(ListCreateAPIView):
    queryset = Label.objects.order_by('created_at')
    serializer_class = LabelSerializer


class RetrieveUpdateDestroyLabelView(RetrieveUpdateDestroyAPIView):
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
