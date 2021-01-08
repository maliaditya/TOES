from django.contrib import admin
from . models import User,WorkerDetails,JobDetails,Categories,RecruitersRequests,WorkersRequests
# Register your models here.

admin.site.register(User)
admin.site.register(WorkerDetails)
admin.site.register(JobDetails)
admin.site.register(Categories)
admin.site.register(RecruitersRequests)
admin.site.register(WorkersRequests)
