from rest_framework import serializers
from .models import Customer, Account, Transaction, ATM, ATMTransaction


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'city']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'date_opened', 'current_balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount',
                  'transaction_date', 'transaction_type']


class ATMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATM
        fields = ['id', 'location', 'current_balance']


class ATMTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATMTransaction
        fields = ['id', 'amount', 'account', 'date']
