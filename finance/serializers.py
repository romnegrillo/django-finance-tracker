from rest_framework import serializers
from finance.models import Wallet, Income, Expense


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"

class IncomeSerializer(serializers.ModelSerializer):
    wallet = serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())

    class Meta:
        model = Income
        fields = "__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    wallet = serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    class Meta:
        model = Expense
        fields = "__all__"
