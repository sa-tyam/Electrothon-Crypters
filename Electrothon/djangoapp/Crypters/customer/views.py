from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from datetime import date
from . import forms
from accounts.models import UserProfile

from blockchainpart.models import Chain

User = get_user_model()

verification_flag = False

# Create your views here.

def CustomerHome (request):
    username = request.user.username
    u = User.objects.get(username=username)

    if u.is_staff:
        return redirect('bank:bank_home')

    customer_type = ''
    if u.userprofile.user_type == 'shopkeeper':
        customer_type = 'shopkeeper'

    loan_list = []
    main_list = []

    amount_list = []
    emi_list = []
    emi_start_date_list = []
    emi_end_date_list = []
    period_list = []
    interest_list = []
    issue_date_list = []
    end_date_list = []

    temp_list = u.loan_set.all()
    today = date.today()
    if temp_list:
        for item in temp_list:
            end_date = item.end_date
            print(end_date)
            print(today)
            if end_date>today:
                print("yes")
                loan_list.append(item)

    if loan_list:
        for item in loan_list:
            amount = item.amount
            print(amount)
            amount_list.append(amount)
            emi_amount = item.emi_amount
            emi_list.append(emi_amount)
            period = item.period
            period_list.append(period)
            interest = item.interest
            interest_list.append(interest)
            issue_date = item.issue_date
            issue_date_list.append(issue_date)
            end_date = item.end_date
            end_date_list.append(end_date)
            temp_emi_list = item.emi_set.all()
            if temp_emi_list:
                for e in temp_emi_list:
                    if e.start_date<=today and e.end_date>=today:
                        st_date = e.start_date
                        emi_start_date_list.append(st_date)
                        en_date = e.end_date
                        emi_end_date_list.append(en_date)

    main_list = zip (amount_list, emi_list, period_list, interest_list, issue_date_list, end_date_list, emi_start_date_list, emi_end_date_list)

    return render (request, 'customerHome.html', {'main_list':main_list, 'customer_type':customer_type})

def CustomerHistory (request):
    username = request.user.username
    u = User.objects.get(username=username)

    customer_type = ''
    if u.userprofile.user_type == 'shopkeeper':
        customer_type = 'shopkeeper'

    loan_list = []

    amount_list = []
    emi_list = []
    period_list = []
    interest_list = []
    issue_date_list = []
    end_date_list = []

    temp_list = u.loan_set.all()
    if temp_list:
        for item in temp_list:
            amount = item.amount
            print(amount)
            amount_list.append(amount)
            emi_amount = item.emi_amount
            emi_list.append(emi_amount)
            period = item.period
            period_list.append(period)
            interest = item.interest
            interest_list.append(interest)
            issue_date = item.issue_date
            issue_date_list.append(issue_date)
            end_date = item.end_date
            end_date_list.append(end_date)

    loan_list = zip (amount_list, emi_list, period_list, interest_list, issue_date_list, end_date_list)

    trans_list = []
    trans_amount_list = []
    trans_depositor_list = []
    trans_time_list = []

    trans_temp_list = u.customertransactions_set.all()
    if trans_temp_list:
        for item in trans_temp_list:
            trans_amt = item.amount
            trans_amount_list.append(trans_amt)
            depositor = item.depositor
            trans_depositor_list.append(depositor)
            trans_time = item.created_at
            trans_time_list.append(trans_time)

    trans_list = zip (trans_amount_list, trans_depositor_list, trans_time_list)

    return render (request, 'customerHistory.html', {'loan_list': loan_list, 'customer_type':customer_type, 'trans_list':trans_list})

def CustomerProfile (request):

    username = request.user.username
    u = User.objects.get(username=username)
    name = u.userprofile.name
    email = u.email
    date_of_birth = u.userprofile.date_of_birth
    age =u.userprofile.age
    gender = u.userprofile.gender
    profession =u.userprofile.profession
    user_type = u.userprofile.user_type
    mobile_number =u.userprofile.mobile_number
    additional_mobile_number =u.userprofile.additional_mobile_number
    address =u.userprofile.address
    city = u.userprofile.city
    state =u.userprofile.state
    pin_code =u.userprofile.pin_code
    balance = u.userprofile.balance

    return render (request, 'customerProfile.html', {
        "username":username,
        "email":email,
        'name':name,
        'date_of_birth':date_of_birth,
        'age':age,
        'gender':gender,
        'profession':profession,
        'user_type':user_type,
        'mobile_number':mobile_number,
        'additional_mobile_number':additional_mobile_number,
        'address':address,
        'city':city,
        'state':state,
        'pin_code':pin_code,
        'balance':balance,
    })

def GetNumberOfOther (request):
    phone = ''
    if request.POST.get('username'):
        user_name = request.POST.get('username')
        if user_name:
            request.session.modified = True
            request.session['otheruser'] = str(user_name)
            us = User.objects.get(username=user_name)
            phone =us.userprofile.mobile_number


    username = request.user.username
    u = User.objects.get(username=username)

    customer_type = ''
    if u.userprofile.user_type == 'shopkeeper':
        customer_type = 'shopkeeper'

    loan_list = []
    main_list = []

    amount_list = []
    emi_list = []
    emi_start_date_list = []
    emi_end_date_list = []
    period_list = []
    interest_list = []
    issue_date_list = []
    end_date_list = []

    temp_list = u.loan_set.all()
    today = date.today()
    if temp_list:
        for item in temp_list:
            end_date = item.end_date
            print(end_date)
            print(today)
            if end_date>today:
                print("yes")
                loan_list.append(item)

    if loan_list:
        for item in loan_list:
            amount = item.amount
            print(amount)
            amount_list.append(amount)
            emi_amount = item.emi_amount
            emi_list.append(emi_amount)
            period = item.period
            period_list.append(period)
            interest = item.interest
            interest_list.append(interest)
            issue_date = item.issue_date
            issue_date_list.append(issue_date)
            end_date = item.end_date
            end_date_list.append(end_date)
            temp_emi_list = item.emi_set.all()
            if temp_emi_list:
                for e in temp_emi_list:
                    if e.start_date<=today and e.end_date>=today:
                        st_date = e.start_date
                        emi_start_date_list.append(st_date)
                        en_date = e.end_date
                        emi_end_date_list.append(en_date)

    main_list = zip (amount_list, emi_list, period_list, interest_list, issue_date_list, end_date_list, emi_start_date_list, emi_end_date_list)

    return render (request, 'customerHome.html', {'main_list':main_list, 'customer_type':customer_type, 'phone':phone})

def Verified (request):
    if not request.session.get('otheruser', None):
        msg = "no other user found"
        return redirect('landing_page')
    else:
        otherusername = request.session['otheruser']
        username = request.user.username
        u = User.objects.get(username=username)
        user_prof = UserProfile.objects.get(user=u)
        other_u = User.objects.get(username=otherusername)
        other_user_prof = UserProfile.objects.get(user=other_u)
    if request.method == 'POST':
        trans_form = forms.CustomerTransactionsForm(data=request.POST)
        if trans_form.is_valid():
            transaction = trans_form.save(commit=False)
            transaction_other = trans_form.save(commit=False)
            amt = transaction.amount
            amt = int(amt)
            user_amt = u.userprofile.balance
            other_user_amt = other_u.userprofile.balance
            if user_amt and amt:
                if amt <= user_amt:
                    other_user_prof.balance = other_user_amt - amt
                    user_prof.balance = user_amt + amt
                    other_user_prof.save()
                    user_prof.save()
                    user_chain = user_prof.chain
                    user_chain.add(ammount_transferred=amt, remaining_balance=user_prof.balance)
                    user_chain.save()
                    other_user_chain = other_user_prof.chain
                    other_user_chain.add(ammount_transferred=amt, remaining_balance=other_user_prof.balance)
                    other_user_chain.save()
                    transaction.user = u
                    transaction.depositor = other_u.username
                    transaction.save()
        return CustomerHome(request)
    else:
        trans_form = forms.CustomerTransactionsForm()
    return render (request, 'transactionpage.html', {'trans_form':trans_form})
