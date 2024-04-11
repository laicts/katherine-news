from django.contrib import admin
from .models import Reader, Author, Editor

# Register your models here.

@admin.register(Reader) 
class adminUsers(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'register_date', 'birth_date']
    search_fields = ['username', 'name']
    list_filter = ['register_date']

