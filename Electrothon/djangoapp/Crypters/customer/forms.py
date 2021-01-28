from django import forms
from . import models

class CustomerTransactionsForm (forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['user', 'depositor',]
        model = models.CustomerTransactions
