from django.db import models

# Create your models here.

class OrderModel(models.Model):
    contact_bio = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(auto_created=True)
    address = models.CharField(max_length=100)
    count = models.IntegerField()
    user_id = models.IntegerField()
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.date_of_order