"""task_manager URL Configuration

https://djoser.readthedocs.io/en/latest/authentication_backends.html
Djoser provides this urls:
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

Djoser endpoints: https://djoser.readthedocs.io/en/latest/base_endpoints.html
"""

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.views import APIView, Response
from task_manager.celery import debug_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('task_manager.apps.user.urls')),
    path('api/v1/labels/', include('task_manager.apps.label.urls')),
    path('api/v1/statuses/', include('task_manager.apps.status.urls')),
    path('api/v1/tasks/', include('task_manager.apps.task.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]


# TODO: Remove it. Just for test handle
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        result = debug_task()
        return Response({'status': 'ok', 'task': result})


urlpatterns += [
    path('api/v1/test/', TestView.as_view())
]
