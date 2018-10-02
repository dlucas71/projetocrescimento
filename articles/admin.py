from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'start_date']
    search_fields = ['title', 'slug']
    Prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
