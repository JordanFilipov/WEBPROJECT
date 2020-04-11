from django.conf.urls import url
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.register, name="register"),
]