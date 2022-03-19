from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    message = 'NoOwner. You have not permission for this action'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsModeratorPermission(permissions.BasePermission):
    message = 'NoModerator. You have not permission for this action'

    def has_permission(self, request, view):
        if request.user.role == "moderator":
            return True
        return False
