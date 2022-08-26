"""Serializers."""

from rest_framework import serializers

from task_manager.apps.label.serializers import LabelSerializer
from task_manager.apps.user.serializers import UserSerializer
from task_manager.apps.status.serializers import StatusSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)
    author = UserSerializer()
    executor = UserSerializer()
    status = StatusSerializer()

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'author',
            'executor',
            'labels',
        )

    def set_author(self, author_pk: int):
        """Add author for task object.
        :param author_pk: author pk (id)
        """

        self.instance.author_id = author_pk
