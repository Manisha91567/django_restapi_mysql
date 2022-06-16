from django.db import models

# Create your models here.

class Tutorial(models.Model):
    Book_title=models.CharField(max_length=70, blank=False, default='')
    Book_author = models.CharField(max_length=200,blank=False, default='')
    Page_numbers=models.CharField(max_length=200,blank=False, default='')
    Prize=models.CharField(max_length=200,blank=False, default='')
    Ratings=models.CharField(max_length=200,blank=False, default='')
   