from django.shortcuts import render
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

# Create your views here.

def CustomerHome (request):
    username = request.user.username
    u = User.objects.get(username=username)

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
        for items in loan_list:
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

    return render (request, 'customerHome.html', {'main_list':main_list})

def CustomerHistory (request):
    username = request.user.username
    u = User.objects.get(username=username)

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
    return render (request, 'customerHistory.html', {'loan_list': loan_list})

def CustomerProfile (request):

    username = request.user.username
    u = User.objects.get(username=username)
    name = u.userprofile.name
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

    return render (request, 'customerProfile.html', {
        "username":username,
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
        'pin_code':pin_code
    })
