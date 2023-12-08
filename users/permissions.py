from rest_framework.permissions import BasePermission


class Is_Teacher(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_teacher)


class Is_Student(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_student)


class Is_Admin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
