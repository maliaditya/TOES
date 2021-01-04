from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, AbstractUser
)

''' For Storing Basic User Information ''' 

class User(AbstractUser):
    dob = models.CharField(max_length=255)
    phone = models.CharField(max_length=255,unique=True,blank=False)
    is_admin = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    gender = models.CharField(max_length=255)
    counter = models.IntegerField(default=0,blank=True,null=True)
    address = models.TextField(blank=False)
    smartphone = models.BooleanField(default =True)
    aadhar_no = models.CharField(max_length=255,default=None)
    
   
    REQUIRED_FIELDS = ['counter','isVerified','is_superuser','is_admin','first_name','last_name','username','password',
                        'dob','gender','aadhar_no','address','smartphone']

    USERNAME_FIELD = 'phone'


    def get_username(self):
        return self.phone

class ProfileImage(models.Model):
    profile_image = models.ImageField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
   


''' Storing Worker Details like Categories, Visiting Charges, Experience ''' 

class WorkerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255,blank=True)
    category_1 = models.CharField(max_length=255,blank=True)
    category_1_vc = models.CharField(max_length=255,blank=True)
    category_1_exp = models.IntegerField(blank=True)
    category_2 = models.CharField(max_length=255,blank=True)
    category_2_vc = models.CharField(max_length=255,blank=True)
    category_2_exp = models.IntegerField(blank=True)
    category_3 = models.CharField(max_length=255,blank=True)
    category_3_vc = models.CharField(max_length=255,blank=True)
    category_3_exp = models.IntegerField(blank=True) 




''' Request Status

    id - Status_Name

     1 - Pending
     2 - Accepted
     3 - Rejected
     4 - Applied
'''
class StatusMaster(models.Model):
    status_name = models.CharField(max_length=255)



''' When recruiter creates post it is stored in JobDetails 
    the post data will be provided from JobDetails
    Status Default == pending
'''
class JobDetails(models.Model):
    job_title = models.CharField(max_length=255)
    job_Description = models.CharField(max_length=300)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default = 1) 

''' 
When Worker sends request to Recruiter
In Recruiters requests tab the data from RecruitersRequests will be provided

'''
class RecruitersRequests(models.Model):
    job_detail = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.IntegerField()
    amount = models.IntegerField()
    status = models.IntegerField(default = 1)  

''' 
When Recruiter hits the hire button a request is send to the worker 
In workers requests tab the data from this table will be provided

'''
class WorkersRequests(models.Model):
    job_detail = models.ForeignKey(JobDetails, on_delete= models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.IntegerField()
    status = models.IntegerField(default = 1)  

''' All the work categories data will be stored in this table '''

class Categories(models.Model):
    categories = models.CharField(max_length=255,unique=True)

