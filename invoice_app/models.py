from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    """
    Name: Customer model definition
    """
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', 'Feminine'),
    )

    name = models.CharField(max_length=132)
    email = models.EmailField()
    phone = models.CharField(max_length=132)
    address = models.CharField(max_length=64)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    age = models.CharField(max_length=12)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

class Meta:
    verbose_name = "Customer"
    verbose_name_plural = "Customers"

def __str__(self):
    return self.name
