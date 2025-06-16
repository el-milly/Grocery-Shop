from django.db import models
from django.utils.text import slugify
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

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

class OrderModel(models.Model):
    contact_bio = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)
    count = models.IntegerField()
    user_id = models.IntegerField()
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_of_order.strftime('%Y-%m-%d %H:%M')