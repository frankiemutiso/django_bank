from .models import *


# important imports for creating api views
from .serializers import *

#
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import PermissionDenied


User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(res, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Owner(permissions.BasePermission):
    def has_obj_permission(self, request, view, obj):
        return obj.owner == request.user


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class ATMViewset(viewsets.ModelViewSet):
    queryset = ATM.objects.all()
    serializer_class = ATMSerializer


class ATMTransactionViewset(viewsets.ModelViewSet):
    queryset = ATMTransaction.objects.all()
    serializer_class = ATMTransactionSerializer
