from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Blouse(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    blouse_name = models.CharField(max_length=100)