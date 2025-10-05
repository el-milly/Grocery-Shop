from django.db import models
from kafka import KafkaConsumer
import threading
import json
# Create your models here.



class CartModel(models.Model):
    user_id = models.CharField(max_length=50)
    items = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user_id)
    

def start_kafka_consume():
    consumer = KafkaConsumer(
        bootstrap_servers='broker:9092',
        group_id='cart_service_group',
        auto_offset_reset='earliest',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))

    )
    consumer.subscribe(pattern='.*_events')


    for message in consumer:
        if message.topic == 'user_events' and message.value['event_type'] == 'user_created':
            cart, created = CartModel.objects.get_or_create(
                user_id=message.value['user_id'],
                defaults={'items': []},
            )
        elif message.topic == 'cart_events':
            if message.value['event_type'] == 'item_added':
                cart = CartModel.objects.get(user_id=message.value['user_id'])
                cart.items.append({
                    'name': message.value['name'],
                    'price': message.value['price']
                })
                cart.save()




threading.Thread(target=start_kafka_consume, daemon=True).start()