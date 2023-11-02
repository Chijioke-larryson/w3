from django.urls import path

from . import views





urlpatterns = [
    path('',views.Home),
    path('Product/',views.Product ),
    path('Customer/',views.Customer),
        
]