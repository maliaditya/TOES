import requests
import json 
phone = 9765402942
url = 'http://18.209.19.126/api/otp/{}'.format(phone)
response = requests.get(url)
print("response",response.status_code)