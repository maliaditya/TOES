from django.urls import path,include
from . import views
urlpatterns = [

    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('restricted/',views.restricted),
    
    #User
    # path('register/user', views.UserList.as_view()),
    # path('userdetail/<int:pk>/', views.UserDetail.as_view()),
    
    #Worker_Details
    path('worker/', views.WorkerDetailsList.as_view()),
    path('workerdetail/<int:pk>/', views.WorkerDetail.as_view()),
    
    #Job_Detail
    path('job/', views.JobDetailsList.as_view()),
    path('jobdetail/<int:pk>/', views.JobDetail.as_view()),
    

    #Categories
    path('categories/', views.CategoriesList.as_view()),
    path('categoriesdetail/<int:pk>/', views.CategoriesDetail.as_view()),

  
    #status
    path('status/', views.StatusMasterList.as_view()),
    path('status/<int:pk>', views.StatusMasterDetail.as_view()),

    #Requests Responses
    #recruitersrequests
    path('worker/req/', views.RecruitersRequestsList.as_view()),
    path('worker/req/<int:pk>', views.RecruitersRequestsDetail.as_view()),

    #workerrequests
    path('recruiter/req', views.WorkersRequestsList.as_view()),
    path('recruiter/req/<int:pk>', views.WorkersRequestsDetail.as_view()),


     #Profile Image
    path('profile/image', views.ProfileImageList.as_view()),
    path('profile/image/<int:pk>', views.ProfileImageDetail.as_view()),
]
