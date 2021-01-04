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
from django.core import serializers


@permission_classes([])
@api_view(['GET'])
def get_worker_count(request):
    worker_count = WorkerDetails.objects.all().count()
    user_count = User.objects.all().count()
    recruiter_count = user_count - worker_count
    job_count = JobDetails.objects.all().count()
    accepted_count = JobDetails.objects.filter(status = 2).count()
    return Response(data={"worker_count": worker_count, "recruiter_count" : recruiter_count, "job_count" : job_count , "accepted_count" : accepted_count})




