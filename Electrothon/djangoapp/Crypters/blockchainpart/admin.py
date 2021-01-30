from django.contrib import admin

from . import models

admin.site.register(models.Chain)
admin.site.register(models.Block)
# Register your models here.
