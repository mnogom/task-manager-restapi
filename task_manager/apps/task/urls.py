"""Urls."""

from django.urls import path

from .views import (ListCreateTaskView,
                    RetrieveUpdateDestroyTaskView)


app_name = 'task'
urlpatterns = [
    path('', ListCreateTaskView.as_view(), name='list'),
    path('<int:pk>/', RetrieveUpdateDestroyTaskView.as_view(), name='sample'),
]