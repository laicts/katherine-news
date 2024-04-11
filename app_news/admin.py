from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News) 
class adminNews(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    search_fields = ['title', 'author']
    list_filter = ['publish_date']
