from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='orders',
        on_delete=models.CASCADE
    )
    discount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.id} {self.user.username} {self.discount}"

class Item(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(
        'Order',
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.id} {self.name} {self.quantity} {self.price}"