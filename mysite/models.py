from django.db import models
class name(models.Model):
       # fname : str
       # lname : str
       # data:str
       # search : str
       fname=models.CharField(max_length=100)
       lname=models.CharField(max_length=100)
       search=models.CharField(max_length=100)
       
    