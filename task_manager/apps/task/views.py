"""Views."""

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated  # noqa: F401
from .models import Task
from .serializers import (ReadTaskSerializer,
                          CreateUpdateTaskSerializer)
from .permissions import PermissionsTask


class ListCreateTaskView(ListCreateAPIView):
    permission_classes = (PermissionsTask, )
    queryset = Task.objects.order_by('created_at')
    serializer_read_class = ReadTaskSerializer
    serializer_create_class = CreateUpdateTaskSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_read_class
        if self.request.method == 'POST':
            return self.serializer_create_class
        raise Exception(f'For method "{self.request.method}" serializer not setting upped')


class RetrieveUpdateDestroyTaskView(RetrieveUpdateDestroyAPIView):
    permission_classes = (PermissionsTask, )
    http_method_names = ('get', 'patch', 'delete', 'head', 'options')
    queryset = Task.objects.all()
    serializer_read_class = ReadTaskSerializer
    serializer_create_class = CreateUpdateTaskSerializer
    lookup_url_kwarg = 'pk'
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_read_class
        if self.request.method == 'PATCH':
            return self.serializer_create_class
        raise Exception(f'For method "{self.request.method}" serializer not setting upped')
