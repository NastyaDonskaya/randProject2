from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

class Numbers(models.Model):
    user_name=models.CharField(max_length=100)
    left_num=models.IntegerField()
    right_num = models.IntegerField()
    count_num = models.IntegerField()
    rand_num=models.CharField(max_length=10000)

