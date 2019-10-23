from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), ),
    path('<slug>/', PostDetailView.as_view(), name='post-detail'),
]

app_name = 'blog'
