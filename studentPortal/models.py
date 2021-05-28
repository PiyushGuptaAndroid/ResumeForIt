from django.contrib.auth.models import User
from django.db import models
# import uuid
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


# class MyUUIDModel(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)


class User_Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=CASCADE,default=1)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    DOB = models.DateField()
    phone = models.CharField(max_length=11)
    StreetAddress = models.TextField()
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    pincode = models.IntegerField()
    highestDegree = models.CharField(max_length=20)
    yearOfDegreeCompleted = models.IntegerField()
    institution = models.TextField()
    specification = models.TextField()
