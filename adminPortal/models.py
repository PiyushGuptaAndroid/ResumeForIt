from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.TextField()
    optionA = models.TextField()
    optionB = models.TextField()
    optionC = models.TextField()
    optionD = models.TextField()
    correctOption = models.TextField()
    tag = models.TextField()
