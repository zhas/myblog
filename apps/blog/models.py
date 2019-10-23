from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from martor.models import MartorField


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=127)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(max_length=127)
    markdown = MartorField(_('Text'))
    lang = models.CharField(_('Language'),
                            max_length=2, choices=settings.LANGUAGES)
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)

    page_views = models.PositiveIntegerField(_('Page views'), default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def get_url(self):
        return '/{}/{}/'.format(self.lang, self.slug)
