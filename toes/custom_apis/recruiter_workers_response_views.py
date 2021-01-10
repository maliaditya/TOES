from django.shortcuts import render
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
import requests
import json

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_workers_responses(request , worker_id ):
    cursor = connection.cursor()
    cursor.execute(f'''
    select job_detail_id, recruiter, authapp_recruitersrequests.status ,job_title from 
    authapp_jobdetails INNER JOIN authapp_recruitersrequests ON 
    authapp_jobdetails.id = authapp_recruitersrequests.job_detail_id 
    where worker_id = {worker_id} Order by authapp_recruitersrequests.id  DESC''')
    row1 = cursor.fetchall()
    content= {}
    payload=[]
    for a in row1:
        job_id = a[0]
        recruiter_id = a[1]
        job_title = a[3]
        status1 = a[2]
        if status1 == 2:
            status1 = 'Accepted'
        elif status1 == 3:
            status1 = 'Rejected'
        else:
            status1 = 'Pending'
        # cursor.execute(f'select status_name from authapp_jobdetails j, authapp_statusmaster s where j.id = {job_id} and j.status = s.id')
        # row2 = cursor.fetchall()
        # st_info = row2[0]
        

        cursor.execute(f'select first_name, phone,last_name  from authapp_user where id = {recruiter_id}')
        row3 = cursor.fetchall()


    
        for result in row3:
                content = {
                    'recruiter_fname' : result[0],
                    'recruiter_lname' : result[2],
                    'Job_title' : job_title,
                    'status': status1,
                    'contact_no': result[1]        
                }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_recruiters_responses(request , recruiter_id ):
    cursor=connection.cursor()
    cursor.execute(f'''
    select job_detail_id, worker_id ,authapp_workersrequests.status,job_title from  authapp_jobdetails 
    INNER JOIN authapp_workersrequests ON authapp_jobdetails.id = authapp_workersrequests.job_detail_id 
    where recruiter = {recruiter_id} Order by authapp_workersrequests.id  DESC''')
    row1 = cursor.fetchall()
    content= {}
    payload=[]
    for a in row1:
        job_id = a[0]
        worker_id = a[1]
        job_title = a[3]
        status1 = a[2]
        if status1 == 2:
            status1 = 'Accepted'
        elif status1 == 3:
            status1 = 'Rejected'
        else:
            status1 = 'Pending'
        # cursor.execute(f'select status_name from authapp_jobdetails j, authapp_statusmaster s where j.id = {job_id} and j.status = s.id')
        # row2 = cursor.fetchall()
        # st_info = row2[0]
        

        cursor.execute(f'select first_name, phone ,last_name  from authapp_user where id = {worker_id}')
        row3 = cursor.fetchall()


    
        for result in row3:
                content = {
                    'worker_fname' : result[0],
                    'worker_lname' : result[2],
                    'status': status1,
                    'Job_title' : job_title,
                    'contact_no': result[1]        
                }
        payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)


