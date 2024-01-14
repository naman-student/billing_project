# code for voucher forms
from django.forms import ModelForm, inlineformset_factory
from .models import Voucher, Transaction

class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        # fields = ['date_created']  # Add other necessary fields
        exclude = ['date_created']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['ACCOUNT_NAME', 'transaction_type', 'remarks', 'weight', 'purity', 'wastage']  # Adjust fields as needed

TransactionFormSet = inlineformset_factory(Voucher, Transaction, form=TransactionForm, extra=1)
