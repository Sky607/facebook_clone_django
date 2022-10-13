from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views 


app_name = 'social_app'

urlpatterns = [
    re_path(r'login/$',auth_views.LoginView.as_view(template_name='social_app/login.html'),name="login"),

    re_path(r'logout/$',auth_views.LogoutView.as_view(template_name="thanks.html"),name="logout"),
    re_path(r'signup/$',views.SignUpView.as_view(),name="signup"),
]
