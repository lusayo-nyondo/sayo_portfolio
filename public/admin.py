from django.contrib import admin

from .models import (
    ContactMessage
)

admin.site.register(ContactMessage)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')