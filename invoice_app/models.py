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

class Invoice(models.Model):
    """
    Name: Invoice model definition
    Descriptio:
    author: karim.khattou@univ-tiaret.dz
    """
    INVOICE_TYPE = (
        ('R', 'RECIEVED'),
        ('P', 'PROFORMA INVOICE'),
        ('I', 'INVOICE')
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=100000, decimal_places=2)
    last_updated_date = models.DateTimeField(null=True)
    paid = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    comment = models.TextField(null=True, max_length=1000, blank=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f"{self.customer.name}_{self.invoice_date_time}"

class Article(models.Model):
    """
    Name: Article model definition
    Description:
    Author: karim.khattou@univ-tiaret.dz
    """        
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    quantity = model.IntegerFiled()
    unit_price = models.DecimalField(max_digits=1000, decimal_palces=2)
    total = models.DecimalField(max_digits=1000, decimal_palces=2)