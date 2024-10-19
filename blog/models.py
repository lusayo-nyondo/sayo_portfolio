from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class BlogPostPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=500)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('hero_image'),
        FieldPanel('body'),
    ]
    
class BlogPostIndexPage(Page):
    subpage_types = ['blog.BlogPostPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['posts'] = BlogPostPage.objects.all()
        return context
    
    