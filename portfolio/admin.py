from django.contrib.admin import (
    site
)

from .models import (
    Project,
    Technology,
    PreviewType
)

site.register(PreviewType)
site.register(Project)
site.register(Technology)