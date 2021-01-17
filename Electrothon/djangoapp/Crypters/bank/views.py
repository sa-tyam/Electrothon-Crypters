from django.shortcuts import render

# Create your views here.

def BankHome (request):

    return render (request, 'bankHome.html')

def BankAdmin (request):

    return render (request, 'bankAdmin.html')

def BankNewLoan (request):

    return render (request, 'bankNewLoan.html')

def BankPastLoan (request):

    return render (request, 'bankPastLoan.html')
