from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegistrationForm()
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()

                customer = Customer()
                customer.customer = User.objects.get(
                    username=form.cleaned_data['username'])
                customer.first_name = form.cleaned_data['first_name']
                customer.last_name = form.cleaned_data['last_name']
                customer.national_ID = form.cleaned_data['national_ID']
                customer.email = form.cleaned_data['email']
                customer.gender = form.cleaned_data['gender']
                customer.city = form.cleaned_data['city']
                customer.save()

                account = Account()
                account.user = Customer.objects.get(
                    customer=customer.customer)
                account.date_opened = timezone.now()
                account.save()

                return redirect('login')

        context = {'form': form}

        return render(request, 'django_bank_app/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back {user}')
                return redirect('home')
            else:
                messages.error(request, 'Username or password invalid!')

        return render(request, 'django_bank_app/login.html')


def logout_view(request):
    logout(request)
    messages.success(
        request, f'You have successfully logged out of your account.')
    return redirect('login')


def home(request):
    context = {}
    return render(request, 'django_bank_app/home.html', context)


@login_required(login_url='login')
def profile(request):
    accounts = Account.objects.filter(user=request.user.customer)
    transactions = Transaction.objects.filter(user=request.user.customer)

    paginator = Paginator(transactions, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'accounts': accounts, 'page_obj': page_obj}

    return render(request, 'django_bank_app/profile.html', context)


@login_required(login_url='login')
def withdraw(request):
    accounts = Account.objects.filter(user=request.user.customer)

    context = {'accounts': accounts}

    return render(request, 'django_bank_app/withdraw.html', context)


@login_required(login_url='login')
def withdraw_process(request):
    if request.method == 'POST':
        amount = request.POST.get('withdraw')
        account = Account.objects.get(user=request.user.customer)
        transaction = Transaction()
        transaction.user = request.user.customer
        transaction.amount = amount
        account.previous_balance = account.current_balance
        balance = account.get_balance(transaction.amount, 1)

        if balance == -1:
            messages.error(
                request, f'Insufficient balance! Available balance is Ksh.{account.previous_balance}')

            return redirect('withdraw')
        else:
            account.current_balance = balance
            transaction.transaction_type = 'Withdraw'

            transaction.save()
            account.save()
            messages.success(
                request, f'You have successfully withdrawn Ksh.{transaction.amount} from your account. Current balance: Ksh.{account.current_balance}')

        return redirect('withdraw')


@login_required(login_url='login')
def transfer(request):
    accounts = Account.objects.filter(user=request.user.customer)
    context = {'accounts': accounts}

    return render(request, 'django_bank_app/transfer.html', context)


@login_required(login_url='login')
def transfer_process(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        account = request.POST.get('account')

        try:
            sender_account = Account.objects.get(user=request.user.customer)
            recipient_account = Account.objects.get(pk=account)

            transaction = Transaction()
            transaction.user = request.user.customer
            transaction.amount = amount

            recipient_user = Customer.objects.get(
                customer=recipient_account.user.customer)

            transaction2 = Transaction()
            transaction2.user = recipient_user
            transaction2.amount = amount

        except ObjectDoesNotExist as error:
            messages.error(request, f'{error}')
            return redirect('transfer')

        if recipient_account == sender_account:
            messages.error(request, f'Invalid transfer!')
            return redirect('transfer')
        else:
            sender_account.previous_balance = sender_account.current_balance
            balance = sender_account.get_balance(transaction.amount, 1)
            if balance == -1:
                messages.error(
                    request, f'Insufficient balance! Available balance is {sender_account.current_balance}')
                return redirect('transfer')
            else:
                sender_account.current_balance = balance

                recipient_account.previous_balance = recipient_account.current_balance
                recipient_account.current_balance = recipient_account.get_balance(
                    transaction2.amount, 2)

                transaction2.transaction_type = 'Transfer'
                recipient_account.save()
                transaction2.save()

                transaction.user = request.user.customer
                transaction.transaction_type = 'Transfer'
                sender_account.save()
                transaction.save()

                messages.success(
                    request, f'You have successfully sent Ksh.{transaction.amount} to {recipient_user}. Current balance: Ksh.{sender_account.current_balance}')

                return redirect('transfer')


@login_required(login_url='login')
def atm_withdrawal(request):
    accounts = Account.objects.filter(user=request.user.customer)
    context = {'accounts': accounts}
    return render(request, 'django_bank_app/atm_withdrawal.html', context)


@login_required(login_url='login')
def atm_withdrawal_process(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        atm_code = request.POST.get('code')
        password = request.POST.get('password')

        try:
            account = Account.objects.get(user=request.user.customer)
            atm = ATM.objects.get(pk=atm_code)
            atm_transaction = ATMTransaction()

            atm_transaction.amount = amount

        except ObjectDoesNotExist as error:
            messages.error(request, f'{error}')
            return redirect('atm_withdrawal')

        user = authenticate(
            request, username=request.user.username, password=password)

        if user is not None:
            account.previous_balance = account.current_balance
            atm.previous_balance = atm.current_balance
            atm_balance = atm.get_balance(atm_transaction.amount, 1)
            account_balance = account.get_balance(amount, 1)

            if atm_balance == -1:
                messages.error(request,
                               f'Sorry! The ATM does not have enough money to dispense.')

                return redirect('atm_withdrawal')
            elif account_balance == -1:
                messages.error(request,
                               f'Insufficient balance! Your account balance is Ksh.{account.balance}')

                return redirect('atm_withdrawal')
            else:
                account.current_balance = account_balance
                atm.current_balance = atm_balance

                atm_transaction.account = account
                atm_transaction.atm = atm

                account.save()
                atm.save()
                atm_transaction.save()

                messages.success(
                    request, f'You have succesfully withdrawn Ksh.{atm_transaction.amount} from the ATM.')

                return redirect('atm_withdrawal')

        else:
            messages.warning(request, 'Invalid Password!')

            return redirect('atm_withdrawal')
