from django.db import models


class VerifyOtp(models.Model):
    phone = models.CharField(max_length=255,unique=True)
    otp = models.CharField(max_length=255)