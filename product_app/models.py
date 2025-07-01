from django.db import models
from django.utils.text import slugify
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
