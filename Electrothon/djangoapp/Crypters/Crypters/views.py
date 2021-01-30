from django.shortcuts import render, redirect

def LandingPage (request):

    return render(request, 'LandingPage.html')
