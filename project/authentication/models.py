from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = {
    'user': {
        'friendly_name': 'Usuário',
        'default_page': '/home/',
    },
}

# Create your models here.
class CustomUser(AbstractUser):
    role = models.CharField(
        default='user',
        max_length=50,
        choices=[(role_key, ROLES[role_key]["friendly_name"]) for role_key in ROLES]
    )

