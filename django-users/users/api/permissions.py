from rest_framework.permissions import BasePermission


class IsPostOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == 'POST' or request.user.is_authenticated)
