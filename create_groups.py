import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from crm.models import Service, Campaign, Lead, Contract, ActiveClient

def create_roles():
    # 1. Роль Оператор
    operator_group, _ = Group.objects.get_or_create(name='Оператор')
    operator_perms = [
        Permission.objects.get(codename='add_lead'),
        Permission.objects.get(codename='view_lead'),
        Permission.objects.get(codename='change_lead'),
    ]
    operator_group.permissions.set(operator_perms)

    # 2. Роль Маркетолог
    marketer_group, _ = Group.objects.get_or_create(name='Маркетолог')
    marketer_perms = [
        Permission.objects.get(codename='add_service'),
        Permission.objects.get(codename='view_service'),
        Permission.objects.get(codename='change_service'),
        Permission.objects.get(codename='add_campaign'),
        Permission.objects.get(codename='view_campaign'),
        Permission.objects.get(codename='change_campaign'),
    ]
    marketer_group.permissions.set(marketer_perms)

    # 3. Роль Менеджер
    manager_group, _ = Group.objects.get_or_create(name='Менеджер')
    manager_perms = [
        Permission.objects.get(codename='view_lead'),
        Permission.objects.get(codename='add_contract'),
        Permission.objects.get(codename='view_contract'),
        Permission.objects.get(codename='change_contract'),
        Permission.objects.get(codename='add_activeclient'),
        Permission.objects.get(codename='view_activeclient'),
        Permission.objects.get(codename='change_activeclient'),
    ]
    manager_group.permissions.set(manager_perms)

    print("Группы (роли) успешно созданы и настроены!")

if __name__ == '__main__':
    create_roles()
