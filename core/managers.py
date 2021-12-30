"""Alternative model managers
"""

# Django
from django.db import models


class SuperUserManager(models.Manager):
    """Manager for User model that returns superusers only"""

    def get_queryset(self):
        """Returned queryset"""
        return super().get_queryset().filter(is_superuser=True)
