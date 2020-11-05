from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
from .models import Transaction


class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICE = (('Male', 'Male'), ('Female', 'Female'))

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=True)
    city = forms.CharField(max_length=100, required=True)
    national_ID = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'national_ID',
            'email',
            'gender',
            'city',
            'password1',
            'password2'
        ]
