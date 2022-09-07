import pytest
from rest_framework.test import APIClient
from django.core.management import call_command
from django.urls import reverse_lazy
from task_manager.apps.user.models import User

client = APIClient()

