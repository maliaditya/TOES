from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories, User, ProfileImage
    )
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrive_profileimage(request,user_id):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}' ")
    #cursor.execute(f'select job_description, job_title, worker_id,amount from authapp_recruitersrequests r , authapp_jobdetails j where r.recruiter ={recruiter_id} and j.recruiter_id = r.recruiter')
    cursor.execute(f'select profile_image from authapp_profileimage where user_id= {user_id}')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
        content = {

            'profile_image': f"http://52.201.220.252/media/{data[0]}",

            }
        payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)

