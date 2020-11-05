from django.contrib import admin
from .models import *


admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(ATM)
admin.site.register(ATMTransaction)
