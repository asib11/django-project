from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)

class Customer