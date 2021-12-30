# Django
from django.contrib import admin

# First Party
from core import models

admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Item)
