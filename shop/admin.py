from django.contrib import admin

# Register your models here.
import shop
from shop import models

#Databae Mogrations
admin.register(models.Users)
admin.register(models.Images)