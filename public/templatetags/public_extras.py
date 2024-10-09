from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def get_link_class(request, url, active_class, inactive_class):
    reversed_url = reverse(url)
    current_url = request.path
    
    if reversed_url == current_url:
        return active_class
    else:
        return inactive_class

@register.simple_tag
class SetVarNode(template.Node):
    def __init__(self, new_val, var_name):
        self.new_val = new_val
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = self.new_val
        return ''

import re
@register.tag
def setvar(parser,token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    
    m = re.search(r'(.*?) as (\w+)', arg)
    
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    new_val, var_name = m.groups()
    
    if not (new_val[0] == new_val[-1] and new_val[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    
    return SetVarNode(new_val[1:-1], var_name)