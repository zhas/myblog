from django.views.generic import TemplateView, DetailView
from django.utils.translation import get_language
from .models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.filter(lang=get_language()). \
            order_by('-created')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(lang=get_language())
