#from rest_framework.permissions import BasePermission 

from rest_framework.permissions import IsAuthenticated

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role == 'admin'


class IsAnalystOrAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role in ['analyst', 'admin']


class IsViewer(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role == 'viewer'