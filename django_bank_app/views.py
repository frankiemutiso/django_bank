from .models import *
from django.contrib.auth.models import User
from rest_framework import viewsets

# important imports for creating api views
from .serializers import *

# class based views for creating apis


class UserViewset(viewsets.ModelViewset):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewset(viewsets.ModelViewset):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewset(viewsets.ModelViewset):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class ATMViewset(viewsets.ModelViewset):
    queryset = ATM.objects.all()
    serializer_class = ATMSerializer


class ATMTransactionViewset(viewsets.ModelViewset):
    queryset = ATMTransaction.objects.all()
    serializer_class = ATMTransactionSerializer
