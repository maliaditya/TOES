from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from rest_framework import generics,serializers
from . models import (
    User,WorkerDetails,JobDetails, Categories,
    StatusMaster, RecruitersRequests, WorkersRequests,ProfileImage , 
    )



class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    re_password = serializers.CharField(max_length=100)

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('counter','isblocked','is_superuser','is_admin','username','password',
                        'dob','gender','aadhar_no', 'profile_image','phone','first_name','last_name','smartphone')

class WorkerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        fields = '__all__'


class JobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        

class StatusMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMaster
        fields = '__all__'


class RecruitersRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitersRequests
        fields = '__all__'

class WorkersRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkersRequests
        fields = '__all__'





class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = '__all__'
