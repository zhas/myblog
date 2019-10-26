from itertools import groupby

from django.views.generic import TemplateView, DetailView
from django.utils.translation import get_language
from .models import Post, Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects. \
            filter(lang=get_language(), is_published=True). \
            order_by('-created')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_queryset(self):
        return super().get_queryset(). \
            filter(lang=get_language(), is_published=True)


class ArchivesView(TemplateView):
    template_name = 'archives.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.filter(
            lang=get_language(), is_published=True
        ).order_by('created')
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category = self.get_object()
        context['posts'] = category.post_set.filter(
            is_published=True
        ).order_by('created')
        return context
