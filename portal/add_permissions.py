from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import Q

"""
Gives the first user in the database all permissions needed to add, edit or delete an opportunity
"""
def add_permissions():
    User = get_user_model()
    users = User.objects.all()
    permissions = Permission.objects.filter(Q(codename='can_add_opportunity') | Q(codename='can_edit_opportunity') | Q(codename='can_delete_opportunity'))
    for permission in permissions:
        users[0].user_permissions.add(permission)

add_permissions()