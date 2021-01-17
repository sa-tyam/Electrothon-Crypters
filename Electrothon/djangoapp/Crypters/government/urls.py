# blogs urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'government'

urlpatterns = [
    path('', views.GovtAdmin, name='admin'),
    path('new_loan/', views.GovtNewLoan, name='new_loan'),
    path('new_currency/', views.GovtNewCurrency, name='new_currency'),
]
