import os

from django.db import models

from .validators import validate_icon_file_extension

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    icon = models.FileField(
        upload_to=os.path.join(
            'public',
            'social_links'
        ),
        validators=[validate_icon_file_extension]
    )
    url = models.URLField()
    call_to_action = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.display_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(
        max_length=255
    )
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"