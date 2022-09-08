from rest_framework import permissions


class PermissionsTask(permissions.BasePermission):

    edit_methods = ("PATCH", "DELETE")
    message = "Custom error message."

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if obj.executor == request.user and request.method not in self.edit_methods:
            return True

        return False