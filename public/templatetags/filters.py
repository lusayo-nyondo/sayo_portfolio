from django import template
from django.urls import (
    reverse
)

register = template.Library()

@register.filter(name="is_link_active")
def is_link_active(request, url):
    reversed_url = reverse(url)
    current_url = request.path

    if reversed_url == current_url:
        return True
    else:
        return False