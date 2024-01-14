from django.shortcuts import render, redirect
from .models import Voucher, Transaction
from .forms import VoucherForm, TransactionFormSet

def create_voucher(request):
    if request.method == 'POST':
        form = VoucherForm(request.POST)
        formset = TransactionFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            voucher = form.save()
            for form in formset:
                # Only save if it's a valid individual form
                if form.is_valid() and form.cleaned_data:
                    transaction = form.save(commit=False)
                    transaction.voucher = voucher
                    transaction.save()
            return redirect('voucher_list')  # Redirect to the list of vouchers
    else:
        form = VoucherForm()
        formset = TransactionFormSet()
    return render(request, 'voucher/create_voucher.html', {'form': form, 'formset': formset})

def home(request):
    return render(request, 'voucher/base.html')

