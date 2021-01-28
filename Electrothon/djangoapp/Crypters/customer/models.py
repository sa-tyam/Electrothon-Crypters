from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerTransactions (models.Model):
    user = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    depositor = models.CharField(max_length=200, null=False)
    amount = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['-created_at']
