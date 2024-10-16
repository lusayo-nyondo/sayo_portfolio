from django.urls import path

from .views import (
    index,
    contact
)

app_name = 'public'
urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
]