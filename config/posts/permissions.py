# Django REST Framework
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Check if user is the owner of a post"""
    
    def has_object_permission(self, request, view, obj):
        """Read-only permissions are allowed for any request."""
        if request.method in permissions.SAFE_METHODS:
            return True

        """Write permissions are only allowed to the author of a post."""
        return obj.user == request.user