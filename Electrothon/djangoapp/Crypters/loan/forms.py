from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class LoanCreateForm (forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['user', 'emi_amount', 'end_date', 'block_chain']
        model = models.Loan
        widgets = {
            'end_date': DateInput(),
        }
