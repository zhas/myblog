from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post


class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return [
            'blog:home',
            'blog:archives',
            'blog:about',

        ]

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    protocol = 'https'
    priority = 1.0

    def items(self):
        return Post.objects.order_by('id')


sitemaps = {
    'static': StaticSitemap(),
    'posts': PostSitemap()
}

