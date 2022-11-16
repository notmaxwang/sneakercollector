from django.db import models
from django.urls import reverse

# Create your models here.

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    retail_price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})

