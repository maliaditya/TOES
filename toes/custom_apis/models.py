from django.db import models


class VerifyOtp(models.Model):
    phone = models.CharField(max_length=255)
    otp = models.CharField(max_length=255)