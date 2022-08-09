"""Serializers."""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'executor',
            'labels',
        )

    def set_author(self, author_pk: int):
        """Add author for task object.
        :param author_pk: author pk (id)
        """

        self.instance.author_id = author_pk