from django.contrib import admin
#Custom admin registers
from .models import Images, PostImage


class ImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Images)
class AdminImage(admin.ModelAdmin):
    inlines = [ImageAdmin]
    class Meta:
            model = Images

@admin.register(PostImage)
class AdminPostImage(admin.ModelAdmin):
    pass

