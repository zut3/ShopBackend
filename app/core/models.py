from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, null=False)
    price = models.FloatField(null=False)
    image = models.URLField(null=True)
    description = models.TextField(null=True)
