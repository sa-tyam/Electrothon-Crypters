from django.contrib import auth
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class UserProfile(models.Model):

    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('not defined', 'not defined'),
    )

    USERTYPE = (
        ('farmer', 'farmer'),
        ('shopkeeper', 'shopkeeper'),
    )

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    date_of_birth = models.CharField(max_length=200, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=200, null=False, choices=GENDER)
    profession = models.CharField(max_length=200, null=False)
    user_type = models.CharField(max_length=200, null=False, choices=USERTYPE)
    mobile_number = models.CharField(max_length=13, null=False)
    additional_mobile_number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=300, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    pin_code = models.IntegerField(null=False)

    def __str__(self):
        return self.name
