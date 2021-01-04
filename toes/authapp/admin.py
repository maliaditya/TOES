from django.contrib import admin
from . models import User,WorkerDetails,JobDetails,Categories
# Register your models here.

admin.site.register(User)
admin.site.register(WorkerDetails)
admin.site.register(JobDetails)
admin.site.register(Categories)
