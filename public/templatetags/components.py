from django import template

from django.urls import (
    reverse
)

register = template.Library()

@register.inclusion_tag('public/navbar/menu_item.html', takes_context=True)
def show_navbar_menu_item(context):
    request = context['request']
    reverse_url = context['reverse_url']
    
    is_active = request.path == reverse(reverse_url)
    
    if is_active:
        class_name = 'active'
    else:
        class_name = 'inactive'
    
    link_url = reverse(reverse_url)
    
    context = {
        'url': link_url,
        'class': class_name
    }
    
    return context