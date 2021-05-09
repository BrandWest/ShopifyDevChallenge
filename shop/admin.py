from django.contrib import admin
#Custom admin registers
from .models import Images, PostImage

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['images', 'caption', 'current_user']
    list_filter = ['current_user']
    search_fields = ['current_user']
    model = Images

@admin.register(PostImage)
class AdminPostImage(admin.ModelAdmin):
    pass

