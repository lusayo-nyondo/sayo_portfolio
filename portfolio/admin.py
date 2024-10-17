from django.contrib.admin import (
    site
)

from .models import (
    Project,
    Technology
)

site.register(Project)
site.register(Technology)