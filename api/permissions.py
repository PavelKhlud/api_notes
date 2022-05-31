from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True
