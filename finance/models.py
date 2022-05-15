from django.db import models

# Create your models here.


class Wallet(models.Model):
    wallet_name = models.CharField(max_length=100, default="My Wallet")
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.wallet_name

class Income(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.wallet.wallet_name} - {self.category} - {self.description}"


class Expense(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.wallet.wallet_name} - {self.category} - {self.description}"
