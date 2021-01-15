from rest_framework import serializers
from django.contrib.auth import get_user, get_user_model
from .models import Customer, Account, Transaction, ATM, ATMTransaction

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type": "password"})
    password2 = serializers.CharField(
        write_only=True, label="Confirm password", style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['username', 'phone_number', "password", "password2"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        phone_number = validated_data["phone_number"]
        password = validated_data["password"]
        password2 = validated_data["password2"]

        if phone_number and User.objects.filter(phone_number=phone_number).exclude(username=username).exists():
            raise serializers.ValidationError({
                "email": "Phone number must be unique!"
            })

        if len(password) < 8:
            raise serializers.ValidationError({
                password: "Password should be longer than 8 characters!"
            })

        if password != password2:
            raise serializers.ValidationError({
                password: "Passwords do not match"
            })

        user = User(username=username, phone_number=phone_number)

        user.set_password(password)

        user.save()

        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name',
                  'email', 'phone_number', 'city']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'customer', 'date_opened', 'current_balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'customer', 'amount',
                  'transaction_date', 'transaction_type']


class ATMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATM
        fields = ['id', 'location', 'current_balance']


class ATMTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATMTransaction
        fields = ['id', 'amount', 'account', 'date']
