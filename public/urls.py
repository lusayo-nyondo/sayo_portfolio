from django.urls import path

from .views import (
    index,
    contact,
    projects,
    designs,
    content
)

app_name = 'public'
urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('projects/', projects, name="projects"),
    path('designs/', designs, name="designs"),
    path('content/', content, name="content")
]