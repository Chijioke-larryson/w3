from django.shortcuts import render
from django.views.generic import DetailView, View
from.models import *

from django.http import HttpResponse
from django.conf import settings
import os 

# Create your views here.
class Home(View):
    def get(self, *args, **kwargs):
        slides = Slide.objects.all()
        blogs = Blog.objects.all()
        context ={
            'slides' : slides,
            'blogs' : blogs,
        }
        return render(self.request, 'home.html', context)
    
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


class Blogs(View):
    """
        This contains instructions on how the the blogs page will be delivered
    """
    def get(self, *args, **kwargs):
        blogs = Blog.objects.all()
        context ={
            'blogs' : blogs,
        }
        return render(self.request, 'blogs.html', context)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'home.html'
    # slug_field = 'post_id'
    # slug_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.all().exclude(pk=self.object.id)
        context["blogs"] = blogs
        return context