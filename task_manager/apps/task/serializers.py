"""Serializers."""

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from task_manager.apps.user.serializers import UserSerializer
from task_manager.apps.user.models import User
from task_manager.apps.label.serializers import LabelSerializer
from task_manager.apps.label.models import Label
from task_manager.apps.status.serializers import StatusSerializer
from task_manager.apps.status.models import Status

from .models import Task


class ReadTaskSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    executor = UserSerializer()
    observer = UserSerializer(read_only=True,
                              many=True,
                              required=False)
    status = StatusSerializer(read_only=True,
                              required=False)
    labels = LabelSerializer(read_only=True,
                             many=True,
                             required=False)

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'description',
            'status',
            'author',
            'executor',
            'observer',
            'labels',
        )


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    """TODO: Test if user updated task become author (??)"""
    executor_id = serializers.IntegerField(required=True) # TODO: Switch field to PrimaryKeyRelatedField
    author = serializers.HiddenField(default=CurrentUserDefault())
    observer_ids = serializers.PrimaryKeyRelatedField(required=False,
                                                      queryset=User.objects.all(),
                                                      source='observer',
                                                      many=True)
    status_id = serializers.PrimaryKeyRelatedField(required=False,
                                                   queryset=Status.objects.all(),
                                                   source='status')
    label_ids = serializers.PrimaryKeyRelatedField(required=False,
                                                   queryset=Label.objects.all(),
                                                   source='labels',
                                                   read_only=False,
                                                   many=True)

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'executor_id',
            'author',
            'observer_ids',
            'status_id',
            'label_ids',
        )
