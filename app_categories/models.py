from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
