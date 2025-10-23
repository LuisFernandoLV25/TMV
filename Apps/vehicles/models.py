from django.db import models
from Apps.customers.models import Customer

class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='vehicles')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"
