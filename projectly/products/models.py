from django.db import models


class Product(models.Model):
	name = models.CharField(
		max_length=128,
		null=False,
		blank=False,
	)
	price = models.FloatField(
		null=False,
		blank=False,
		default=0.0,
	)
	quantity = models.IntegerField(
		null=False,
		blank=False,
		default=0,
	)
