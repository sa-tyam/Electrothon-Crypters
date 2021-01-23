from django.db import models

# Create your models here.

class TransactionAmount (models.Model):
    transaction_amount = models.IntegerField(null=False)
