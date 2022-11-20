from django.db import models
from django.urls import reverse


# Create your models here.

class Shoelace(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('shoelace_detail', kwargs={'pk': self.id})

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    retail_price = models.IntegerField()
    shoelaces = models.ManyToManyField(Shoelace)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})


class Cleaned(models.Model):
    date = models.DateField('Sneaker Cleaned Date')
    product = models.TextField(default="N/A")
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cleaned {self.sneaker.name} on {self.date} with {self.product}"

    class Meta:
        ordering = ['-date']

