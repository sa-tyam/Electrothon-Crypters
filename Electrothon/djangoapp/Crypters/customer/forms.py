from django.contrib.auth.models import User
from django import forms
from . import models

class TransactionAmountForm (forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.TransactionAmount
