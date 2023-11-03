
from django.db import models 
import sys
sys.path.append('/path/to/your/module')


class Slide(models.Model):
    title = models.CharField(max_length= 30)
    image = models.ImageField(upload_to='slides/', default="media/slide.jpg", blank=True, null=True)

    def __str__ (self):
        return f"{self.title}"
# Create your models here.




class Body (models.Model):
    title = models.CharField(max_length= 30)

    def __str__ (self):
        return f"{self.title}"
    
    
class Contact(models.Model):
    title = models.CharField(max_length= 30)

    def __str__ (self):
        return f"{self.title}"
# Create your models here.
# Create your models here.


class Blog(models.Model):
    '''
        Model your blog contents here by collecting all the information you need concerning a blog post
    '''
    title = models.CharField(max_length= 30)
    image = models.ImageField(upload_to='post/', default="media/post.jpg", blank=True, null=True)
    body = models.TextField(max_length=300, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__ (self):
        return f"{self.title}"