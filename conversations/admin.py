from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):
    """Conversations Admin Definitions"""

    list_display = ("__str__", "count_messages", "count_participants")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Messages Admin Definitions"""

    list_display = ("__str__", "created")

