from django.db import models
# Create your models here.



class CartModel(models.Model):
    user_id = models.IntegerField()
    items = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
