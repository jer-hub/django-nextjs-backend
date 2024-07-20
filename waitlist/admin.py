from django.contrib import admin
from .models import WaitListEntry
# Register your models here.
@admin.register(WaitListEntry)
class WaitListEntryAdmin(admin.ModelAdmin):
    list_display = ["email"]