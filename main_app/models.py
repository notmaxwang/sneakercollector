from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    retail_price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})


class Shoelace(models.Model):
    date = models.DateField('Shoelace Changed Date')
    color = models.TextField(default="red")
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"Switch {self.sneaker.name} shoelaces on {self.date} to color {self.color}"

    class Meta:
        ordering = ['-date']

