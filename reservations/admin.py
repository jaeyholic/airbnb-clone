from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservations)
class Reservations(admin.ModelAdmin):
    """Reservations Admin Definitions"""

    pass

