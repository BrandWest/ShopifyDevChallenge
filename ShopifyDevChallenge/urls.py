"""ShopifyDevChallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from PyQt5.QtCore.QUrl import url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
#custom views
from shop import views
from shop.views import ImageRepoView, UserLoginView, UserSignupView, ImageUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', UserLoginView.as_view(), name="login"),
    path('commons/signup/', UserSignupView.as_view(), name='signup'),
    path('', ImageUploadView, name='image_repo'),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', include('shop.urls')),
    path('commons/repo', ImageRepoView, name="repo"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)