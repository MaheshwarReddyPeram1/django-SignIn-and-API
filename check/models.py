from django.db import models

# Create your models here.

class Courses(models.Model):
    courseName              =models.CharField(max_length=50)
    titleName               =models.CharField(max_length=200)
    tags                    =models.CharField(max_length=50)
    color1                  =models.CharField(max_length=10)
    color2                  =models.CharField(max_length=10)
    from_age                =models.IntegerField()
    to_age                  =models.IntegerField()
    

    