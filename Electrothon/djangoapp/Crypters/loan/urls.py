from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'loan'

urlpatterns = [
    path('new_loan/', views.IssueLoan, name='new_loan'),
]
