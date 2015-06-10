from django.contrib import admin
from myapp.models import Article
# Register your models here.


def make_published(modeladmin, request, queryset):
	print dir(modeladmin)
	queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'status']
	ordering = ['title']
	actions = [make_published]

admin.site.register(Article, ArticleAdmin)