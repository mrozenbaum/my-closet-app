from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

from . import views



app_name='users'
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]

