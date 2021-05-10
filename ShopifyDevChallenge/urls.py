#ShopifyDevChallenge URL Configuration

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

#custom views
from shop.views import ImageRepoView, UserLoginView, UserSignupView, ImageUploadView, ImageDeletionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', UserLoginView.as_view(), name="login"),
    path('commons/signup/', UserSignupView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('commons/repo/', ImageRepoView, name="repo"),
    path('image_repo/', ImageUploadView, name='image_repo'),
    re_path(r'^delete_image/(?P<pk>\d+)/$', ImageDeletionView, name='delete_image'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)