from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories,EmergencyDetails
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
def emergency(request , user_id):
    try:
        info = EmergencyDetails.objects.get(user = user_id)
        data = {
            "id":info.id,
            "emergency_contact" : info.contact_no
        }
        return Response(data=data, status=200)
    except :
        return Response(data=data, status=400)

