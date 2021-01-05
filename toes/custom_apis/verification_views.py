from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from authapp.models import User
import base64
import requests

# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class SendOtp(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = User.objects.get(phone=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            message = {
                'message': 'Phone Number does exist please enter registered phone number'
            }
            return Response(data = message, status=400)

        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        querystring = {"authorization":"8SxMu8XjX6rpRasOGDY83AoGQzedmJA7wbgGOEgp92XYsWanQBiUx96IIVeU","sender_id":"FSTSMS","language":"english","route":"qt","numbers":f"{Mobile}","message":"42422","variables":"{BB}|{FF}","variables_values":f"{OTP.at(Mobile.counter)}|http://52.201.220.252/api/otp"}
        headers = {
                    'cache-control': "no-cache"
                }

        url = "https://www.fast2sms.com/dev/bulk"

        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)


