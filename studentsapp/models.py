from django.db import models

# Create your models here.



class Students(models.Model):
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    marks=models.IntegerField()
    result=models.CharField(max_length=100)


