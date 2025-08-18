from django.db import models
from kafka import KafkaConsumer
import json
import threading
# Create your models here.

class ProductsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    carbs = models.FloatField()
    fats = models.FloatField()
    protein = models.FloatField()
    kcal = models.FloatField()


    def __str__(self):
        return self.name


def kafka_consumer():
    consumer = KafkaConsumer('created-product',group_id='created-products',bootstrap_servers='broker:9092', 
    value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    for message in consumer:
        if message.value['event-type'] == 'created-product':
            ProductsModel.objects.create(name=message.value['name'],
            category=message.value['category'], slug=message.value['slug'],
            price=message.value['price'], description=message.value['description'],
            carbs=message.value['carbs'], fats=message.value['fats'],
            protein=message.value['protein'], kcal=message.value['kcal'])

thread = threading.Thread(target=kafka_consumer, daemon=True)
thread.start()