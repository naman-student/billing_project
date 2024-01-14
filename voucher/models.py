from django.db import models

class CustomerAccount(models.Model):
    # Add fields for your customer account here
    name = models.CharField(max_length=100)
    # email = models.EmailField()
    phone = models.CharField(max_length=15)
    # address = models.TextField()
    # account no 
    account_no = models.IntegerField(unique=True)
    

    def __str__(self):
        return self.name
    
#hi

# model for transactions    
class Transaction(models.Model):
    # DATE = models.DateField()
    # date
    DATE = models.DateField(auto_now_add=True)
    ACCOUNT_NAME = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    TRANSACTION_TYPE_CHOICES = [
        ('ISSUE', 'Issue'),
        ('RECEIVE', 'Receive'),
        # Add other transaction types as needed
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    remarks = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    purity = models.DecimalField(max_digits=5, decimal_places=2)
    wastage = models.DecimalField(max_digits=5, decimal_places=2)
    # voucher = models.ForeignKey('Voucher', on_delete=models.CASCADE, null=True, blank=True)
    voucher_no = models.ForeignKey('Voucher', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def pure_gold(self):
        return self.weight * (self.purity / 100)

    @property
    def pure_gold_balance(self):
        return self.weight * ((self.purity + self.wastage) / 100)
    
class Voucher(models.Model):
    date_created = models.DateField(auto_now_add=True)
    transactions = models.ForeignKey('Transaction', on_delete=models.CASCADE)

    def __str__(self):
        return f"Voucher {self.id} - {self.date_created}"
