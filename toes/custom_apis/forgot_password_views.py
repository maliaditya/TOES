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

def enter_otp(request):
    if request.method == 'POST':

        otp = request.POST.get('otp')
        try:
            mobile = VerifyOtp.objects.get(otp=otp)
            if mobile.otp == otp:
                VerifyOtp.objects.filter(otp=otp).delete()
                return redirect('reset')
            else:
                messages.error(request,'OTP not correct')
        except:
            messages.error(request,'OTP not correct')
    return render(request , 'custom_apis/enterotp.html')




def passreset(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        
        if re_password == password:
            u = User.objects.get(phone = phone)
            u.set_password(password)
            u.save()
            messages.success(request,'Password Successfully changed')
        else:
            messages.error(request,"Password do not match")

    return render(request , 'custom_apis/resetpassword.html')




