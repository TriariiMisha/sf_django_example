from rest_framework import permissions


class BasePermission(permissions.BasePermission):
    message = 'Please, request role in our nice system.'

    def has_permission(self, request, view):
        return True

        # print(message)
        # return False
