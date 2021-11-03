from django.db import models

from cdhometask.choices import GENDER_CHOICES


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    annual_income = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    salary = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    experience = models.IntegerField(default=0, blank=True, null=True)
