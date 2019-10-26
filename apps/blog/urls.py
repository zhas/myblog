from django.urls import path
from .views import IndexView, PostDetailView, ArchivesView, \
    AboutView, CategoryDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('archives/', ArchivesView.as_view(), name='archives'),
    path('about/', AboutView.as_view(), name='about'),
    path('category/<slug>/', CategoryDetailView.as_view(), name='category'),

    # that should be placed in the end
    path('<slug>/', PostDetailView.as_view(), name='post-detail'),
]

app_name = 'blog'
