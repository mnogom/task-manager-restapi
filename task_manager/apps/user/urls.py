from django.urls import path
from .views import UserList

app_name = 'user'
urlpatterns = [
    path('', UserList.as_view(), name='list'),
]
