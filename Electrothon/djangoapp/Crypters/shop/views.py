from django.shortcuts import render

# Create your views here.

def ShopHome (request):

    return render (request, 'shopHome.html')

def ShopHistory (request):

    return render (request, 'shopHistory.html')

def ShopProfile (request):

    return render (request, 'shopProfile.html')
