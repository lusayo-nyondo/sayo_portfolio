import os

from django.db import models

from .validators import (
    validate_icon_file_extension
)

class PreviewType(models.Model):
    icon = models.FileField(
        upload_to=os.path.join(
            'portfolio',
            'preview_types'
        ),
        validators=[validate_icon_file_extension]
    )
    name = models.CharField(
        max_length=100
    )
    display_name = models.CharField(
        max_length=100
    )
    
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_on = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.display_name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to=os.path.join('portfolio', 'projects')
    )
    preview_url = models.URLField()
    preview_type = models.ForeignKey(
        'PreviewType',
        on_delete=models.DO_NOTHING
    )
    
    technologies = models.ManyToManyField(
        'Technology',
        blank=True
    )
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    CATEGORIES = [
        ('frontend', 'Frontend Tools'),
        ('backend', 'Backend Tools'),
        ('fullstack', 'Fullstack Frameworks'),
        ('mobile', 'Mobile Frameworks'),
        ('crossplatform', 'Crossplatform Frameworks'),
        ('database', 'Databases'),
        ('data_engineering', 'Data Engineering Tools'),
        ('devops', 'Dev Ops Tools'),
        ('language', 'Languages'),
        ('content_management_systems', 'Content Management Systems'),
        ('other', 'Other')
    ]
    
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    icon = models.FileField(
        upload_to=os.path.join('portfolio', 'technologies'),
        validators=[validate_icon_file_extension],                         
    )
    
    category = models.CharField(
        max_length=100,
        choices=CATEGORIES,
        default='other'
    )
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'technologies'
    
    def __str__(self):
        return self.display_name