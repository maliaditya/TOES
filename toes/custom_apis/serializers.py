from .models import *
from rest_framework import generics,serializers
from . models import VerifyOtp


class VerifyOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyOtp
        fields = '__all__'