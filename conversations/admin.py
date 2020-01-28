from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):
    """Conversations Admin Definitions"""

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Messages Admin Definitions"""

    pass
