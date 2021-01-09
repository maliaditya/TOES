from django.contrib import messages
from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
# Create your views her
from authapp.models import  User
from requests.auth import HTTPBasicAuth
import requests
import json
from uuid import uuid4
from rest_framework.views import APIView
from .models import VerifyOtp
from django.core.exceptions import ObjectDoesNotExist
import math, random 
def enter_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            a = VerifyOtp.objects.get(otp=otp)
            if int(a.otp) == int(otp):
                return redirect('reset')
            else:
                messages.error(request,'OTP not correct')
        except ObjectDoesNotExist:
            messages.error(request,'OTP not correct')
        
    return render(request , 'custom_apis/enterotp.html')




def passreset(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        try:
            VerifyOtp.objects.get(phone = phone)
            if re_password == password:
                u = User.objects.get(phone = phone)
                u.set_password(password)
                u.save()
                messages.success(request,'Password Successfully changed')
                VerifyOtp.objects.filter(phone = phone).delete()
            else:
                messages.error(request,"Password do not match")
        except ObjectDoesNotExist:
            messages.error(request,'Please enter the number on which you got the otp!')


    return render(request , 'custom_apis/resetpassword.html')




def generateOTP(): 
    digits = "123456789"
    OTP = "" 
    for i in range(6): 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 

def send_otp(phone):
    Mobile = User.objects.get(phone=phone) 
    otp = generateOTP()
    try:
        VerifyOtp.objects.filter(phone = phone).delete()
    except ObjectDoesNotExist:
        pass
    a = VerifyOtp(phone = phone , otp = otp )
    a.save()
    querystring = {"authorization":"8SxMu8XjX6rpRasOGDY83AoGQzedmJA7wbgGOEgp92XYsWanQBiUx96IIVeU","sender_id":"FSTSMS","language":"english","route":"qt","numbers":f"{Mobile}","message":"42422","variables":"{BB}|{FF}","variables_values":f"{otp}|http://52.201.220.252/api/otp"}
    headers = {
                    'cache-control': "no-cache"
                }

    url = "https://www.fast2sms.com/dev/bulk"

    requests.request("GET", url, headers=headers, params=querystring)




def verify_phone(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        try:
            User.objects.get(phone = phone)
            send_otp(phone=phone)
            return redirect('enterotp')
        except ObjectDoesNotExist:
            messages.error(request,'Phone No. Does Not Exist')
        
    return render(request , 'custom_apis/verify_number.html')



