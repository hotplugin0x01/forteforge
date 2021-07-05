from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField()
    postal_code = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    portfolio = models.FileField()


class Enterprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    function = models.CharField(max_length=100)
    work_email = models.EmailField()
    postal_code = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    requirement = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    frequency = models.CharField(max_length=50, null=True)
    requirement_deadline = models.DateField()
    facilitation = models.CharField(max_length=50, null=True)
    attendance = models.CharField(max_length=50, null=True)
