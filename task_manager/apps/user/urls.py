from django.urls import path
from .views import (UserList,
                    RetrieveUserView)

app_name = 'user'
urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('<int:pk>/', RetrieveUserView.as_view(), name='sample'),
]
