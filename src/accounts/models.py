from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    customerID = models.OneToOneField(User, related_name="customer", blank=False, null=False, on_delete=models.CASCADE, help_text="ID for the desired customer to be looked up.")
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=2)

    def save(self, *args, **kwargs):
        credit = self.balance
        customerID = self.customerID

        try:
            account = Account.objects.get(customerID=customerID)
        except:
            super().save(*args, **kwargs)

        if credit != 0:
            new_transaction = Transaction.objects.create(accountID=self, amount=credit)
            new_transaction.save()


class Transaction(models.Model):
	accountID = models.ForeignKey(Account, related_name="transactions", blank=False, null=False, on_delete=models.CASCADE, help_text="ID for the desired customer to be looked up.")
	amount = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	date = models.DateTimeField(auto_now=True)
