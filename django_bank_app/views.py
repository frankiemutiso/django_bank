from django.shortcuts import render, redirect


def index(request):
    return render(request, 'django_bank_app/index.html', context=None)
