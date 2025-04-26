from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    message = 'Please, request role our nice system.'

    def has_permission(self, request, view):
        return True
