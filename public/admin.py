from django.contrib import admin

from .models import (
    ContactMessage,
    SocialLink
)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')


admin.site.register(SocialLink)    
admin.site.register(ContactMessage, ContactMessageAdmin)
