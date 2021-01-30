from django.shortcuts import render
from loan.models import Loan
from blockchainpart import models as bc_model
from accounts.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

def BankHome (request):

    return render (request, 'bankHome.html')

def BankAdmin (request):

    main_list = []

    time_stamp_list = []
    index_list = []
    ammount_transferred_list = []
    remaining_balance_list = []
    hash_list = []
    previous_hash_list = []
    chain_list = []
    nonce_list = []

    block_set = bc_model.Block.objects.all()
    if block_set:
        for item in block_set:
            time_stamp = item.time_stamp
            time_stamp_list.append(time_stamp)
            index = item.index
            index_list.append(index)
            ammount_transferred = item.ammount_transferred
            ammount_transferred_list.append(ammount_transferred)
            remaining_balance = item.remaining_balance
            remaining_balance_list.append(remaining_balance)
            hash = item.hash
            hash_list.append(hash)
            previous_hash = item.previous_hash
            previous_hash_list.append(previous_hash)
            chain = item.chain
            chain_list.append(chain)
            nonce = item.nonce
            nonce_list.append(nonce)

    main_list = zip (time_stamp_list, index_list, ammount_transferred_list, remaining_balance_list, hash_list, previous_hash_list, chain_list, nonce_list)

    return render (request, 'bankAdmin.html', {'main_list':main_list})

def GetUserBlock (request):
    if request.POST.get('username'):
        user_name = request.POST.get('username')
        if user_name:
            u = User.objects.get(username=user_name)
            chain = bc_model.Chain.objects.get(user=u)
            block_set = chain.block_set.all()

    else:
        return BankAdmin(request)

    main_list = []

    time_stamp_list = []
    index_list = []
    ammount_transferred_list = []
    remaining_balance_list = []
    hash_list = []
    previous_hash_list = []
    chain_list = []
    nonce_list = []

    if block_set:
        for item in block_set:
            time_stamp = item.time_stamp
            time_stamp_list.append(time_stamp)
            index = item.index
            index_list.append(index)
            ammount_transferred = item.ammount_transferred
            ammount_transferred_list.append(ammount_transferred)
            remaining_balance = item.remaining_balance
            remaining_balance_list.append(remaining_balance)
            hash = item.hash
            hash_list.append(hash)
            previous_hash = item.previous_hash
            previous_hash_list.append(previous_hash)
            chain = item.chain
            chain_list.append(chain)
            nonce = item.nonce
            nonce_list.append(nonce)

    main_list = zip (time_stamp_list, index_list, ammount_transferred_list, remaining_balance_list, hash_list, previous_hash_list, chain_list, nonce_list)

    return render (request, 'bankAdmin.html', {'main_list':main_list})

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
