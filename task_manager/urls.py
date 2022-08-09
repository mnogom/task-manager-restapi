"""task_manager URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.apps.user.urls')),
    path('labels/', include('task_manager.apps.label.urls')),
    path('statuses/', include('task_manager.apps.status.urls')),
    path('task/', include('task_manager.apps.task.urls')),
    path('auth/', obtain_auth_token, name='auth'),
]
