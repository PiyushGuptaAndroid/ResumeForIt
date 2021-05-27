from django.db import models

# Create your models here.


class Recruiter(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    
class Club(models.Model):
    name = models.CharField(max_length=20)
    money=models.IntegerField(max_length=200)
    