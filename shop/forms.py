from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):
    """ this is account User model"""

    def __str__(self):
        return "@{}".format(self.username)