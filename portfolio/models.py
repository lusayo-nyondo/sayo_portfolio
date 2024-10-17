import os

from django.db import models

from .validators import (
    validate_icon_file_extension
)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to=os.path.join('portfolio', 'projects')
    )
    url = models.URLField()
    is_demo = models.BooleanField(default=False)
    technologies = models.ManyToManyField(
        'Technology',
        blank=True
    )
    
    @property
    def technologies_list(self):
        content = ', '.join([ f'"{ t.display_name }"' for t in self.technologies.all()])
        print(content)
        return content

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    CATEGORIES = [
        ('frontend', 'Frontend Frameworks'),
        ('backend', 'Backend Frameworks'),
        ('fullstack', 'Fullstack Frameworks'),
        ('mobile', 'Mobile Frameworks'),
        ('crossplatform', 'Crossplatform Frameworks'),
        ('database', 'Databases'),
        ('data_engineering', 'Data Engineering Tools'),
        ('devops', 'Dev Ops Tools'),
        ('language', 'Languages'),
        ('other', 'Other'),
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