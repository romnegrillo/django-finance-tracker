from django.shortcuts import render
from django.http import JsonResponse

from finance.serializers import WalletSerializer, IncomeSerializer, ExpenseSerializer
from finance.models import Wallet, Income, Expense

from rest_framework import generics

class WalletRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "pk"

class WalletListAPIView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletCreateAPIView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def perform_create(self, serializer):
        serializer.save()

class WalletUpdateAPIView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()

class WalletDeleteAPIView(generics.DestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# ----------------------------------------------------------------

class IncomeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = "pk"

class IncomeListAPIView(generics.ListAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class IncomeCreateAPIView(generics.CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def perform_create(self, serializer):
        serializer.save()

class IncomeUpdateAPIView(generics.UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()

class IncomeDeleteAPIView(generics.DestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# ----------------------------------------------------------------

class ExpenseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = "pk"

class ExpenseListAPIView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseCreateAPIView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save()

class ExpenseUpdateAPIView(generics.UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        serializer.save()

class ExpenseDeleteAPIView(generics.DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)