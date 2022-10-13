"""second_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path(r'^$',views.IndexView.as_view(), name='index'),
    re_path(r'^social_app/',include("social_app.urls"),name='social_app'),
    re_path(r'^social_app/',include("django.contrib.auth.urls")),
    re_path(r'^success/$',views.TestPage.as_view(), name='success'),
    re_path(r'^thanks',views.ThanksPage.as_view(), name='thanks'),
    re_path(r"^posts/", include("posts.urls", namespace="posts")),
    re_path(r"^groups/",include("groups.urls", namespace="groups")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
