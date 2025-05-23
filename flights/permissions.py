from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffReadOnlySuperuserFullAcess(BasePermission):
    """
    - Permite leitura (GET, HEAD, OPTIONS) para usuários is_staff.
    - Permite todas as ações para is_superuser.
    - Usuários que não são parte de admin são negados.
    """

    def has_permission(self, request, view):
        user = request.user

        if user and user.is_authenticated and user.is_superuser:
            return True
        
        if user and user.is_authenticated and user.is_staff:
            return request.method in SAFE_METHODS
        
        return False