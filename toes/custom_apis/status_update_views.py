from django.shortcuts import render
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json



#RESPONSES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recruiters_response(request,st, job_id):
    cursor=connection.cursor()
    cursor.execute(f' update authapp_recruitersrequests set status = {st} where job_detail_id = {job_id}')
    cursor.execute(f'update authapp_jobdetails set status = {st} where id = {job_id}')
    if st == 2:
        payload = {"message" : "request accepted "}
    elif st == 3:
        payload = { "message" : "request rejected "}
    return Response(data =payload,status = status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def workers_response(request, st,job_id):
    cursor=connection.cursor()
    cursor.execute(f'update authapp_workersrequests set status = {st} where job_detail_id = {job_id}')
    cursor.execute(f'update authapp_jobdetails set status = {st} where id = {job_id}')
    if st == 2:
        payload = {"message" : "request accepted "}
    elif st == 3:
        payload = { "message" : "request rejected "}
    return Response(data =payload,status = status.HTTP_200_OK)
  