from django.db import models
from Apps.users.models import CustomUser

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True, verbose_name="Documento")
    birth_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()
