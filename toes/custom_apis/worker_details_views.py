from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories
    )
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json
# from authapp import views

# Create your views here.
# Select specific Rolecity

# class WorkerCustomAPI:
    
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)


#Display workers info by specific Category

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_by_category(request,category):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}' ")
    cursor.execute(f"select  first_name, phone, city, category_1, category_1_vc, category_1_exp, category_2, category_2_vc, category_2_exp,category_3,category_3_vc,category_3_exp, authapp_user.id from authapp_user INNER JOIN authapp_workerdetails ON authapp_user.id = authapp_workerdetails.user_id where category_1 = '{category}' OR category_2 = '{category}' OR category_3 = '{category}'")

    row = cursor.fetchall()
    content = {}
    payload = []
    for result in row:
        if result[3] == f'{category}' :
            # api = f'http://127.0.0.1:8000/userdetail/{result[11]}/'
            # user_info = requests.get(api, )
            # print(user_info.json())
            content = { 'worker_name': result[0], 
                        'contact_no': result[1],
                        'category':result[3],
                        'visiting_charges':result[4],
                        'experience':result[5],
                        'Worker_id':result[12],
                        }
            payload.append(content)
        elif  result[6] == f'{category}':
            content = {  'worker_name': result[0], 
                        'contact_no': result[1],
                        'category':result[6],
                        'visiting_charges':result[7],
                        'experience':result[8],
                        'Worker_id':result[12],
                        }
            payload.append(content)
        else:
            content = { 'worker_name': result[0], 
                        'contact_no': result[1],
                        'category':result[9],
                        'visiting_charges':result[10],
                        'experience':result[11],
                        'Worker_id':result[12],
                        }
            payload.append(content)

    return Response(data=payload, status=status.HTTP_200_OK)

#Display all the workers regardless of there category
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_all(request):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details")
    cursor.execute('select  first_name, phone, city, category_1, category_1_vc, category_1_exp, category_2, category_2_vc, category_2_exp, category_3, category_3_vc, category_3_exp,last_name  from authapp_user INNER JOIN authapp_workerdetails ON authapp_user.id = authapp_workerdetails.user_id')

    row = cursor.fetchall()
    content = {}
    payload = []
    for result in row:
        content = {  'fname': result[0],
                    'lname': result[12],  
                    'phone': result[1],
                    'city': result[2],
                    'category_1': result[3],
                    'category_1_vc':result[4],
                    'category_1_ex':result[5],
                    'category_2': result[6],
                    'category_2_vc':result[7],
                    'category_2_ex':result[8],
                    'category_3': result[9],
                    'category_3_vc':result[10],
                    'category_3_ex':result[11],
            }
        payload.append(content)

    
    return Response(data=payload, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specific_worker_details(request,user_id):
    cursor=connection.cursor()
    #cursor.execute(f"select * from authapp_worker_Details")
    cursor.execute(f'select * from authapp_workerdetails where user_id = {user_id}')

    row = cursor.fetchall()
    content = {}
    payload = []
    for result in row:
        content = {  'id': result[0], 
                    'city': result[1],
                    'category_1': result[2],
                    'category_1_vc':result[3],
                    'category_1_exp':result[4],
                    'category_2': result[5],
                    'category_2_vc':result[6],
                    'category_2_exp':result[7],
                    'category_3': result[8],
                    'category_3_vc':result[9],
                    'category_3_exp':result[10],
                    'user_id':result[11],
            }
        payload.append(content)

    
    return Response(data=payload, status=status.HTTP_200_OK)



@permission_classes([IsAuthenticated])
@api_view(['GET'])
def display_all_withoutsmartphone(request):
    cursor=connection.cursor()
    cursor.execute('select first_name, phone, city, category_1, category_1_vc, category_1_exp, category_2, category_2_vc, category_2_exp, category_3, category_3_vc, category_3_exp,smartphone ,last_name from authapp_user INNER JOIN authapp_workerdetails ON authapp_user.id = authapp_workerdetails.user_id')

    row = cursor.fetchall()
    content = {}
    payload = []
    for result in row:
      if result[12] == True :
        content = {  'fname': result[0],
                        'lname': result[13],
                    'phone': result[1],
                    'city': result[2],
                    'category_1': result[3],
                    'category_1_vc':result[4],
                    'category_1_ex':result[5],
                    'category_2': result[6],
                    'category_2_vc':result[7],
                    'category_2_ex':result[8],
                    'category_3': result[9],
                    'category_3_vc':result[10],
                    'category_3_ex':result[11],

                    }
        payload.append(content)


    return Response(data=payload, status=status.HTTP_200_OK)




