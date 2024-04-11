from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category) 
class adminNews(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
