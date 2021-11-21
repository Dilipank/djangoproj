from django.db import models


class Collector(models.Model):
    company = models.TextField()
    symbol = models.CharField(max_length=10)
    price = models.IntegerField()
