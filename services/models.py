import os
from django.db import models

from portfolio.validators import (
    validate_icon_file_extension
)

class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(
        upload_to=os.path.join('services', 'thumbnails'),
        validators=[validate_icon_file_extension],
    )
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name