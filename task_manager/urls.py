"""task_manager URL Configuration

https://djoser.readthedocs.io/en/latest/authentication_backends.html
Djoser provides this urls:
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
"""

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('task_manager.apps.user.urls')),
    path('api/v1/labels/', include('task_manager.apps.label.urls')),
    path('api/v1/statuses/', include('task_manager.apps.status.urls')),
    path('api/v1/tasks/', include('task_manager.apps.task.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]
