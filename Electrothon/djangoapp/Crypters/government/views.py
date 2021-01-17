from django.shortcuts import render

# Create your views here.

def GovtAdmin (request):

    return render (request, 'govtAdmin.html')

def GovtNewLoan (request):

    return render (request, 'govtNewLoan.html')

def GovtNewCurrency (request):

    return render (request, 'govtNewCurrency.html')
