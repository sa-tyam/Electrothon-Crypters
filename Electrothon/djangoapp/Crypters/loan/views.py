from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

from . import models
from accounts.models import UserProfile

from . import forms

def IssueLoan(request):
    if request.method == 'POST':
        loan_form = forms.LoanCreateForm(data=request.POST)

        if loan_form.is_valid():
            username = request.POST.get('username')
            user = User.objects.get(username=username)
            user_prof = UserProfile.objects.get(user=user)
            loan = loan_form.save(commit=False)
            user_prof.balance = user_prof.balance + loan.amount
            user_prof.save()
            loan.user = user
            p = loan.amount
            r = loan.interest/100
            t = loan.period
            time_for_loop = loan.period
            emi = (p*r*pow(1+r,t))/(pow(1+r,t)-1)
            loan.emi_amount = emi
            date_v = date.today()
            loan.end_date = date_v +  relativedelta(months =+ t)
            loan.save()

            for x in range(time_for_loop):
                emi = models.Emi()
                emi.loan = loan
                date_var = loan.issue_date
                emi.amount = loan.emi_amount
                emi.start_date = date_var + relativedelta(months =+ x)
                emi.end_date = date_var + relativedelta(months=+(x+1))
                emi.save()

            return redirect('bank:bank_home')
    else:
        loan_form = forms.LoanCreateForm()

    return render (request, 'loan/loancreate.html',{
        'loan_form':loan_form,
    })
