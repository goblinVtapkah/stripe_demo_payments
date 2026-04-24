from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Item(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField()
	price = models.DecimalField(
		max_digits=10,
		decimal_places=2,
	)
	currency = models.CharField(
		max_length=3,
		choices=[
			("USD", "USD"),
			("EUR", "EUR"),
		],
		default="USD",
	)

class Discount(models.Model):
	item = models.OneToOneField(
		Item,
		on_delete=models.CASCADE,
		related_name="discount",
	)
	percent = models.DecimalField(
		max_digits=5,
		decimal_places=2,
		validators=[
			MinValueValidator(0),
			MaxValueValidator(100),
		],
	)