from django.db import models

# Create your models here.

class OrderModel(models.Model):
    contact_bio = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(auto_created=True)
    address = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        return self.date_of_order