from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='posts'

urlpatterns = [
    re_path(r"^$", views.PostList.as_view(), name="all"),
    re_path(r"new/$", views.CreatePost.as_view(), name="create"),
    re_path(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    re_path(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    re_path(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]+ static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)
