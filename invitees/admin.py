from django.contrib import admin
from .models import Invitee


@admin.register(Invitee)
class InviteeAdmin(admin.ModelAdmin):
    list_display = ("name", "side", "relationship", "guest_count", "events_invited", "created_at")
    list_filter = ("side", "relationship", "events_invited")
    search_fields = ("name",)
    ordering = ("name",)
