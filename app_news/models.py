from django.db import models
from app_users.models import Author, Editor
from app_categories.models import Category

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=5000)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=14)

    publish_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to="images/", null=True, blank=True)
