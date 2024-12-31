from django.db import models

from wagtail.models import Page  # type: ignore
from wagtail.fields import StreamField  # type: ignore
from wagtail.blocks import (  # type: ignore
    RichTextBlock,
    StructBlock,
    ChoiceBlock,
    TextBlock
)
from wagtail.admin.panels import FieldPanel  # type: ignore
from wagtail.search import index  # type: ignore

import pygments  # type: ignore
from pygments import (  # type: ignore
    lexers,
    formatters
)


class CodeBlock(StructBlock):
    current_lexer = None

    language_choices = []

    for lexer in lexers.get_all_lexers():
        try:
            language_choices.append(
                (lexer[1][0], lexer[1][0])
            )
        except IndexError:
            continue

    language = ChoiceBlock(
        choices=language_choices,
        default='plain'
    )
    code = TextBlock(
        form_classname='monospace'
    )

    class Meta:
        template = 'blog/blocks/code_block.html'

    def get_context(
        self,
        value,
        parent_context=None
    ):
        context = super().get_context(
            value,
            parent_context=parent_context
        )
        lexer = lexers.get_lexer_by_name(
            value='language'
        )
        formatter = formatters.HtmlFormatter()
        highlighted_code = pygments.highlight(
            value['code'],
            lexer,
            formatter
        )
        context['highlighted_code'] = pygments.highlight(
            highlighted_code
        )
        return context


class BlogPostPage(Page):
    date: models.DateField = models.DateField("Post date")
    intro: models.CharField = models.CharField(
        max_length=500
    )
    hero_image: models.ForeignKey = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body: StreamField = StreamField(
        [
            ('rich_text', RichTextBlock()),
            ('code', CodeBlock()),
        ],
        blank=True
    )
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
