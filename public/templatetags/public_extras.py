from django.template import (
    Library as TemplateLibrary,
    Node as TemplateNode,
    TemplateSyntaxError
)

from django.urls import reverse

register = TemplateLibrary()

@register.simple_tag
def get_navbar_link_class(request, url, active_class, inactive_class):
    reversed_url = reverse(url)
    current_url = request.path
    
    is_url_part_of_current_url = current_url.startswith(reversed_url)
    
    print(reversed_url)
    if reversed_url == '/':
        if reversed_url == current_url:
            return active_class
        else:
            return inactive_class
    elif is_url_part_of_current_url:
        return active_class
    else:
        return inactive_class

@register.simple_tag
class SetVarNode(TemplateNode):
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
        raise TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    
    m = re.search(r'(.*?) as (\w+)', arg)
    
    if not m:
        raise TemplateSyntaxError("%r tag had invalid arguments" % tag_name)
    new_val, var_name = m.groups()
    
    if not (new_val[0] == new_val[-1] and new_val[0] in ('"', "'")):
        raise TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    
    return SetVarNode(new_val[1:-1], var_name)