from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    bio = models.TextField()
    union_member = models.BooleanField(default=False)
