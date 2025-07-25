from django.db import models
from kafka import KafkaConsumer
import threading
import json
# Create your models here.



class CartModel(models.Model):
    user_id = models.IntegerField(unique=True)
    items = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
    

def start_kafka_consume():
    consumer = KafkaConsumer(
        'user-events',
        bootstrap_servers=['broker:9092'],
        group_id='cart_service_group',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))

    )
    for message in consumer:
        if message.value['event_type'] == 'user_created':
            cart, created = CartModel.objects.get_or_create(
                user_id=message.value['user_id'],
                defaults={'items': []}
            )
threading.Thread(target=start_kafka_consume, daemon=True).start()