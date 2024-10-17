from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    CATEGORIES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('data_engineering', 'Data Engineering'),
        ('dev_ops', 'Dev Ops')
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(
        max_length=250,
        choices=CATEGORIES
    )
    
    class Meta:
        verbose_name_plural = 'technologies'