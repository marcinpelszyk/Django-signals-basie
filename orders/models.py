from django.db import models

from cars.models import Car
class Order(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car)
    total = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.name)

