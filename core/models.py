# Django
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Local
from . import managers


class User(AbstractUser):
    """Customized user"""

    objects = UserManager()
    supers = managers.SuperUserManager()

    class Meta:
        """User's meta"""

        verbose_name = _("User")
        verbose_name_plural = _("Users")
        default_manager_name = "objects"


class Category(models.Model):
    """Category to which an item belongs"""

    objects = models.Manager()

    display_name = models.CharField(max_length=255)

    class Meta:
        """Category's Meta"""

        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.display_name)

    def get_absolute_url(self):
        """Returns preffered url for the resource"""
        return reverse("category_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    """Item to exchange or giveaway"""

    objects = models.Manager()

    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=555)
    categories = models.ManyToManyField("Category")

    class Meta:
        """Item's Meta"""

        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return str(self.display_name)

    def get_absolute_url(self):
        """Returns preffered url for the resource"""
        return reverse("item_detail", kwargs={"pk": self.pk})
