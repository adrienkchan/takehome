from django.db import models

# Create your models here.

class Asset(models.Model):
    asset_name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    price = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    description = models.TextField()
    cert_verification = models.BooleanField(default=False)
