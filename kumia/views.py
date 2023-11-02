from django.shortcuts import render
from django.views.generic import DetailView, View
from.models import Slide

from django.http import HttpResponse
from django.conf import settings
import os 

# Create your views here.
class Home(View):
    def get(self, *args, **kwargs):
        slides = Slide.objects.all()
        context ={
            'slides' : slides,
        }
        return render(self.request, 'head.html', context)
    
# Create your views here.
class Body(View):
    def get(self, *args, **kwargs, ):
        slides = Slide.objects.all()
        context ={
            'slides' : slides,
        }
    
        
        return render(self.request, 'blog.html', context)
    
class Contact(View):
     def get(self, *args, **kwargs):
        slides = Slide.objects.all()
        context ={
            'slides' : slides,
        }
        return render(self.request, 'contact.html', context)