from rest_framework import permissions

class IsOrganizer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user.userprofile
