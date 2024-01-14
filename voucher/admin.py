from django.contrib import admin
from .models import CustomerAccount, Transaction, Voucher

# Register your models here.

admin.site.register(CustomerAccount)
admin.site.register(Transaction)
admin.site.register(Voucher)


