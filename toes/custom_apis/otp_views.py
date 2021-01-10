from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from authapp.models import User
import base64
import requests
from .models import VerifyOtp
from .serializers import VerifyOtpSerializer
import math, random 
from django.shortcuts import render,redirect
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
import requests
import json


def generateOTP(): 
    OTP = random.randint(1000,9999)
    return OTP 

@api_view(['GET'])
@permission_classes([])
def send_otp(request,phone):
    try:
        Mobile = User.objects.get(phone=phone) 
        otp = generateOTP()
        val = VerifyOtp.objects.filter(phone=phone).exists()
        if val == True:
            VerifyOtp.objects.filter(phone = phone).update(otp = otp)
        else:
            a = VerifyOtp(phone = phone , otp = otp )
            a.save()

        querystring = {"authorization":"8SxMu8XjX6rpRasOGDY83AoGQzedmJA7wbgGOEgp92XYsWanQBiUx96IIVeU","sender_id":"FSTSMS","language":"english","route":"qt","numbers":f"{Mobile}","message":"42422","variables":"{BB}|{FF}","variables_values":f"{otp}|http://65.1.2.12/api/otp"}
        headers = {
                    'cache-control': "no-cache"
                }

        url = "https://www.fast2sms.com/dev/bulk"

        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response({"otp": otp}, status=200)  # Just for demonstration

    except ObjectDoesNotExist:
        message = {
                'message': 'Phone Number does exist please enter registered phone number'
            }
        return Response(data = message, status=400)


@api_view(['GET'])
@permission_classes([])
def verify_otp(request, phone, otp):
    mobile = VerifyOtp.objects.get(phone=phone)
    if mobile.otp == otp:
        VerifyOtp.objects.filter(phone=phone).delete()
        return Response("correct", status=200)
    return Response("OTP is wrong", status=400)


