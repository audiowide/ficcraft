
from rest_framework.permissions import (BasePermission, 
                                        IsAuthenticated, 
                                        IsAdminUser)

# Permissions some
class CreateOnlyPermission(BasePermission):
    def has_permission(self, request, view):
         if request.method == 'POST':
            return IsAuthenticated().has_permission(request, view)
         elif request.method == 'PUT':
            return IsAuthenticated().has_permission(request, view)
         elif request.method == 'DELETE':
            return IsAuthenticated().has_permission(request, view)
         return True

# Admin permissions
class AdminPermission(BasePermission):
    def has_permission(self, request, view):
         if request.method == 'POST':
            return IsAdminUser().has_permission(request, view)
         elif request.method == 'PUT':
            return IsAdminUser().has_permission(request, view)
         elif request.method == 'DELETE':
            return IsAdminUser().has_permission(request, view)
         return True