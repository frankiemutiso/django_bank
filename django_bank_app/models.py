from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_opened = models.DateTimeField(default=timezone.now)
    previous_balance = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    current_balance = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Withdraw', 'Withdraw'), ('Transfer', 'Transfer'))
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
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


class ATMTransaction(models.Model):
    atm = models.ForeignKey(
        ATM, on_delete=models.CASCADE, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)
