from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def CustomerHome (request):

    return render (request, 'customerHome.html')

def CustomerHistory (request):

    return render (request, 'customerHistory.html')

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
