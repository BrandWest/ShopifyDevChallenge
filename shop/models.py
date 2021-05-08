from django.contrib.auth.models import User
from django.db import models

class Images(models.Model):
    caption = models.CharField(max_length=250)
    images = models.ImageField(upload_to=".")
    current_user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.caption

class PostImage(models.Model):
    image = models.ForeignKey(Images, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='.')

    def __str__(self):
        return self.Images.caption