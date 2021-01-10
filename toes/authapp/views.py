from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import  (
    User, WorkerDetails, JobDetails, Categories, StatusMaster, WorkersRequests,EmergencyDetails,
    RecruitersRequests ,ProfileImage
    ) 
from authapp.serializers import (
    UserCreateSerializer, WorkerDetailsSerializer, JobDetailsSerializer, CategoriesSerializer,
    EmergencyDetailsSerializer,StatusMasterSerializer, WorkersRequestsSerializer,
    RecruitersRequestsSerializer, ProfileImageSerializer
    )
 




''' basic server testing api  not related to projects '''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request):
    return Response(data="Login Requied To Access This Page!", status=status.HTTP_200_OK)


# ''' User '''
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

''' Worker_Details '''
class WorkerDetailsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkerDetails.objects.all()
    serializer_class = WorkerDetailsSerializer

class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkerDetails.objects.all()
    serializer_class = WorkerDetailsSerializer

''' Job_Details ''' 
class JobDetailsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = JobDetails.objects.all()
    serializer_class = JobDetailsSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = JobDetails.objects.all()
    serializer_class = JobDetailsSerializer

''' Categories '''
class CategoriesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


''' Status Master '''
class StatusMasterList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StatusMaster.objects.all()
    serializer_class = StatusMasterSerializer

class StatusMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StatusMaster.objects.all()
    serializer_class = StatusMasterSerializer


''' Recturiters Requests '''
class RecruitersRequestsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RecruitersRequests.objects.all()
    serializer_class = RecruitersRequestsSerializer

class RecruitersRequestsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RecruitersRequests.objects.all()
    serializer_class = RecruitersRequestsSerializer


''' Workers Requests '''
class WorkersRequestsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkersRequests.objects.all()
    serializer_class = WorkersRequestsSerializer

class WorkersRequestsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkersRequests.objects.all()
    serializer_class = WorkersRequestsSerializer


''' Profile Image '''
class ProfileImageList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer

class ProfileImageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer


''' Emergency Details '''
class EmergencyDetailsList(generics.ListCreateAPIView):
    permission_classes = []
    queryset = EmergencyDetails.objects.all()
    serializer_class = EmergencyDetailsSerializer

class EmergencyDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = EmergencyDetails.objects.all()
    serializer_class = EmergencyDetailsSerializer

