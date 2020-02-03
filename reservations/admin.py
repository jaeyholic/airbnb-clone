from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reservations)
class Reservations(admin.ModelAdmin):
    """Reservations Admin Definitions"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guests",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
