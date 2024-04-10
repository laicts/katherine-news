from django.db import models
from app_news.models import News

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
class CategoryHasNews(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)