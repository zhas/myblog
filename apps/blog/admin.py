from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    model = Post
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'slug', 'title']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
