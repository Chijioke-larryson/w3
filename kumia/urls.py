
from django.urls import path
from . import views
from.views import *
app_name ='kumia'

urlpatterns =[ 
  
    path('', Home.as_view(),name ='home'),
    path('blog/', Body.as_view(),name ='blog'),
      # path('contact <str:Read_more>/', Contact.as_view(),name ='contact'),
    path('blogs/', Blogs.as_view(),name ='blogs'),
    path('blog/<pk>/', BlogDetailView.as_view(), name='blog_detail'),
      
]
