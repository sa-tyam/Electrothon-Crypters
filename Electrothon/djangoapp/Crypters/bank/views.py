from django.shortcuts import render
from loan.models import Loan
# Create your views here.

def BankHome (request):

    return render (request, 'bankHome.html')

def BankAdmin (request):

    return render (request, 'bankAdmin.html')

def BankNewLoan (request):

    return render (request, 'bankNewLoan.html')

def BankPastLoan (request):
    main_list = []
    user_list = []
    username_list = []
    amount_list = []
    emi_amount_list = []
    period_list = []
    interest_list = []
    issue_date_list = []
    end_date_list = []

    loan_set = Loan.objects.all()
    if loan_set:
        for item in loan_set:
            user = item.user
            user_list.append(user)
            username = item.username
            username_list.append(username)
            amount = item.amount
            amount_list.append(amount)
            emi_amount = item.emi_amount
            emi_amount_list.append(emi_amount)
            period = item.period
            period_list.append(period)
            interest = item.interest
            interest_list.append(interest)
            issue_date = item.issue_date
            issue_date_list.append(issue_date)
            end_date = item.end_date
            end_date_list.append(end_date)

    main_list = zip (user_list, username_list, amount_list, emi_amount_list, period_list, interest_list, issue_date_list, end_date_list)

    return render (request, 'bankPastLoan.html', {'main_list':main_list})
