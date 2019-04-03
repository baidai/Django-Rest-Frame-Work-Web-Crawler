from django.db import models

# Create your models here.
class Subject(models.Model): 
    name = models.CharField(max_length =100)
    color = models.CharField(max_length =100)
    
    def __str__(self):
        return self.name 

class Author(models.Model):
    author = models.CharField(max_length =100)
    picture = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.author 
    
class Article(models.Model):
    title = models.CharField(max_length =100)
    slug = models.SlugField(max_length =100)
    author = models.CharField(max_length =100, default= 'Some String')
    subject = models.CharField(max_length =100)
    hero_image = models.ImageField(null=True, blank=True)#pip install Pillow
    publish_date =models.DateTimeField(auto_now_add =True)
    content =  models.TextField(max_length =200) # unrestricted text
     
    def __str__(self):
        return self.title

