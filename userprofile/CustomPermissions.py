from rest_framework.permissions import BasePermission

class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, user_obj):
        return request.user.is_staff or user_obj==request.user