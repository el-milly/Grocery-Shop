from django.db import models
from django.utils.text import slugify
# Create your models here.


class OrderModel(models.Model):
    contact_bio = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100)
    count = models.IntegerField()
    product_id = models.UUIDField()

    def __str__(self):
        return self.date_of_order.strftime('%Y-%m-%d %H:%M')