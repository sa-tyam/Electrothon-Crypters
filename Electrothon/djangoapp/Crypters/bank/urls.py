# blogs urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'bank'

urlpatterns = [
    path('', views.BankHome, name='bank_home'),
    path('admin/', views.BankAdmin, name='admin'),
    path('new_loan/', views.BankNewLoan, name='new_loan'),
    path('past_loan/', views.BankPastLoan, name='past_loan'),
    path('get_user_block/', views.GetUserBlock, name='get_user_block'),
]
