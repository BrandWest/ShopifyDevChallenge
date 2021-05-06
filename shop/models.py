from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    user_email = models.CharField(max_length=100) #Make exceptions for invalid
    password = models.CharField(max_length=500) #Fix to be used with hash, salts, etc
    is_admin = models.IntegerField() # 0 = False, 1 = True
    user_join_date = models.DateTimeField("Date Joined")

class Images(models.Model):
    image_size = models.FloatField()
    image_count = models.IntegerField()
