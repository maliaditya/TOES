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
def block(request,st,user_id):
    cursor=connection.cursor()
    cursor.execute(f' update authapp_user set isblocked = {st} where id = {user_id}')
    return Response(data = {"message": "user blocked success"},status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delete1(request,user_id):
    User.objects.filter(id=user_id).delete()
    return Response(status = status.HTTP_200_OK)
