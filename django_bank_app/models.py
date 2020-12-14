from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
import uuid


class Customer(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'))

    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254,  null=True, blank=True)
    gender = models.CharField(
        max_length=50, choices=GENDER, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    national_ID = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name}'


class Account(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_opened = models.DateTimeField(default=timezone.now)
    previous_balance = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    current_balance = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)

    def get_balance(self, amount, code):
        amount = Decimal(amount)
        previous_balance = self.previous_balance
        current_balance = self.current_balance

        if code == 1:
            if previous_balance > amount:
                current_balance = previous_balance - amount
                return current_balance
            else:
                return -1

        else:
            current_balance = previous_balance + amount
            return current_balance


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Withdraw', 'Withdraw'), ('Transfer', 'Transfer'))
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    transaction_date = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(
        max_length=50, choices=TRANSACTION_TYPES)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-transaction_date']


class ATM(models.Model):
    previous_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    current_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    def get_balance(self, amount, code):
        amount = Decimal(amount)
        previous_balance = self.previous_balance
        current_balance = self.current_balance

        if code == 1:
            if previous_balance > amount:
                current_balance = current_balance - amount
                return current_balance
            else:
                return -1


class ATMTransaction(models.Model):
    atm = models.ForeignKey(
        ATM, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
