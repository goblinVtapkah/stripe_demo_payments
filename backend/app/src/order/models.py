from django.db import models
from item.models import Item

class Order(models.Model): pass

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
	item = models.ForeignKey(Item, on_delete=models.CASCADE)