
from django.db import models 
import sys
sys.path.append('/path/to/your/module')


class Slide(models.Model):
    title = models.CharField(max_length= 30)

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