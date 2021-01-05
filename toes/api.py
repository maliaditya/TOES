import requests
import json 

data = {
            "counter": 0,
                "isVerified": 0,
                "is_superuser": 0,
                "is_admin": 1,
                "first_name": "admin",
                "last_name": "lname",
                "username": "username",
                "password": "aditya@123",
                "dob":"1998-02-01",
                "gender": "male",
                "aadhar_no": "aadhar",
                "address":"address",
                "smartphone": 0,
                "phone": 987654321456,
                "re_password": "aditya@123"
        }
        
create_user_api = 'http://52.201.220.252/users/'
response = requests.post(create_user_api, json=data)
print("response",response)