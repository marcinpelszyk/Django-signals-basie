from django.db import models

from buyer.models import Buyer


class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return f'{self.name}--{self.price}  {self.buyer}'
