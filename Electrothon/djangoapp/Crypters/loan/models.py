from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Loan (models.Model):
    user =  models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=False)
    amount = models.IntegerField(null=False)
    emi_amount = models.IntegerField(null=False)
    period = models.IntegerField(null=False)
    interest = models.IntegerField(null=False)
    issue_date = models.DateField(auto_now=True, null=False)
    end_date = models.DateField(null=False)
    class Meta:
        ordering = ['-issue_date']

class Emi (models.Model):
    loan = models.ForeignKey(Loan, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    paid_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']
