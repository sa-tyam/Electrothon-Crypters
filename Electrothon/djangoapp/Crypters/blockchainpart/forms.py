from django.contrib.auth.models import User
from django import forms
from . import models


class ChainCreateForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['user']
        model = models.Chain
