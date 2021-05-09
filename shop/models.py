from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Images(models.Model):
    caption = models.CharField(max_length=250)
    images = models.ImageField(upload_to=".")
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True, related_name='user')

    def __str__(self):
        return self.caption

    def delete(self, *args, **kwargs):
        self.images.delete()
        self.caption.delete()
        self.current_user.delete()
        super().delete(*args, **kwargs)

    def get_username(self):
        return self.current_user


class PostImage(models.Model):
    image = models.ForeignKey(Images, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='.')

    def __str__(self):
        return self.Images.caption