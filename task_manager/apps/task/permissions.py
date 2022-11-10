# TODO: Make ability to read task only for observer/executor/author

from rest_framework import permissions


class ChangeByAuthorOnlyPermission(permissions.BasePermission):  # TODO: Rename permission

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        if request.user == obj.executor and request.method == 'PATCH' \
                or request.method in permissions.SAFE_METHODS:
            return True
        return False
