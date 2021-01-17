# blogs urls.py

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ShopHome, name='shop_home'),
    path('history/', views.ShopHistory, name='shop_history'),
    path('profile/', views.ShopProfile, name='shop_profile'),
]
