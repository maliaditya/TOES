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

def enter_otp(request):
    server_url = "http://52.201.220.252"
    localhost_url = "http://127.0.0.1:8000"
    new = "http://18.209.19.126"
    if request.method == 'POST':
        phone = request.POST.get('phone')
        otp = request.POST.get('otp')
         data = {
            "otp":otp,
            "phone":phone,
        }

        url = f'{new}/api/verify'
        response = requests.get(url,data=data)  
        print(response.status_code) 
        if response.status_code == 200:
            return redirect(f'{new}/api/reset_password/{phone}')
        else:
            messages.error(request,'OTP not correct')
    return render(request , 'custom_apis/enterotp.html')




def passreset(request, phone):
    if request.method == 'POST':
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




