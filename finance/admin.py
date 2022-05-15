from django.contrib import admin

from finance.models import Wallet, Income, Expense

# Register your models here.
admin.site.register(Wallet)
admin.site.register(Income)
admin.site.register(Expense)