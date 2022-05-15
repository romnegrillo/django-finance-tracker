from django.urls import path

from . import views

urlpatterns = [
    path("wallet/", views.WalletCreateAPIView.as_view()),
    path("wallet/all/", views.WalletListAPIView.as_view()),
    path("wallet/<int:pk>/", views.WalletRetrieveAPIView.as_view()),
    path("wallet/update/<int:pk>/", views.WalletUpdateAPIView.as_view()),
    path("wallet/delete/<int:pk>/", views.WalletDeleteAPIView.as_view()),

    path("income/", views.IncomeCreateAPIView.as_view()),
    path("income/all/", views.IncomeListAPIView.as_view()),
    path("income/<int:pk>/", views.IncomeRetrieveAPIView.as_view()),
    path("income/update/<int:pk>/", views.IncomeUpdateAPIView.as_view()),
    path("income/delete/<int:pk>/", views.IncomeDeleteAPIView.as_view()),

    path("expense/", views.ExpenseCreateAPIView.as_view()),
    path("expense/all/", views.ExpenseListAPIView.as_view()),
    path("expense/<int:pk>/", views.ExpenseRetrieveAPIView.as_view()),
    path("expense/update/<int:pk>/", views.ExpenseUpdateAPIView.as_view()),
    path("expense/delete/<int:pk>/", views.ExpenseDeleteAPIView.as_view()),
]