from math import degrees
from django.db import models

class Tutors(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=20)
    dob = models.DateField()
    description = models.TextField(max_length=150)
    degreeChoices =[
        ('Ba/BSc.', "Bachelors"),
        ('MSc', "Master"),
        ('Phd', 'Doctoral')
    ]
    degree = models.CharField(choices=degreeChoices)
    major = models.CharField(max_length=20, blank=False, null=False)
    minor = models.CharField(max_length=20, blank =True, null=True)
    subject = models.CharField()
    

