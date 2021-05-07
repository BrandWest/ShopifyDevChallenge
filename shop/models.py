from django.db import models
import datetime
from django.db import models
from django.contrib import auth

class Images(models.Model):
    image_size = models.FloatField()
    image_count = models.IntegerField()

class User(auth.models.User, auth.models.PermissionsMixin):
    """ this is account User model"""

    def __str__(self):
        return "@{}".format(self.username)