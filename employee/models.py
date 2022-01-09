from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    department = models.CharField(max_length=70, blank=False, default='')
    post = models.CharField(max_length=70, blank=False, default='')
    dateOfJoining = models.CharField(max_length=70, blank=False, default='')



