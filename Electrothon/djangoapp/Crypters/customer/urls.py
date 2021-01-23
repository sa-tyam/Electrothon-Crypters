# blogs urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.CustomerHome, name='customer_home'),
    path('history/', views.CustomerHistory, name='customer_history'),
    path('profile/', views.CustomerProfile, name='customer_profile'),
    path('get_number/',views.GetNumberOfOther,name="get_number"),
    path('get_number/verified/',views.Verified,name="verified"),
]
