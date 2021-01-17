from django.shortcuts import render

# Create your views here.

def CustomerHome (request):

    return render (request, 'customerHome.html')

def CustomerHistory (request):

    return render (request, 'customerHistory.html')

def CustomerProfile (request):

    return render (request, 'customerProfile.html')
