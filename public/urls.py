from django.urls import path

from .views import (
    index,
    
    contact,
    contact_result
)

app_name = 'public'
urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('contact/result/', contact_result, name="contact_result"),
]