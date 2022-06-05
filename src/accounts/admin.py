from django.contrib import admin

# Register your models here.

from .models import Account, Transaction

class AccountAdmin(admin.ModelAdmin):
    list_display = ("customerID", "balance")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("accountID", "amount", "date")

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

