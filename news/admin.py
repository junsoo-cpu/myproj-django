from django.contrib import admin

from news.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
