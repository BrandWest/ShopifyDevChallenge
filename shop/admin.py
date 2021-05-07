from django.contrib import admin

# Register your models here.
import shop
from shop import models, views

#Databae Mogrations
admin.register(models.Users)
admin.register(models.Images)
admin.register(views.LoginView_form)