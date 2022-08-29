"""Views."""

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated  # noqa: F401
from .models import Task
from .serializers import TaskSerializer


class ListCreateTaskView(ListCreateAPIView):
    # TODO:
    #  1. Fix create feature. Possible solution:
    #  https://github.com/beda-software/drf-writable-nested
    #  2. Uncomment permission classes after auth feature
    #  permission_classes = (IsAuthenticated,)
    queryset = Task.objects.order_by('created_at')
    serializer_class = TaskSerializer


class RetrieveUpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    # TODO:
    #  1. Fix create feature. Possible solution:
    #  https://github.com/beda-software/drf-writable-nested
    #  2. Uncomment permission classes after auth feature
    #  permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'
