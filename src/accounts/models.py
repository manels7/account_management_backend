from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    customerID = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=2)


class Transaction(models.Model):
    customerID = models.ForeignKey(Account, blank=False, null=False, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
