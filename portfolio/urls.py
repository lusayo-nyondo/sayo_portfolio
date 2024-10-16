from django.urls import path

from .views import (
    index,
    projects,
    designs,
    content
)

app_name = 'portfolio'
urlpatterns = [
    path('', index, name="index"),
    path('projects', projects, name="projects"),
    path('experience', projects, name="experience"),
    path('designs', designs, name="designs"),
    path('content', content, name="content")
]