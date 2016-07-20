from django.conf.urls import url
from . import auth_views, views, profile_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', auth_views.register, name='register'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', profile_views.profile, name='profile'),
    url(r'^\+(?P<username>[\w.-]{1,30})$', profile_views.user_profile, name='user_profile'),
    url(r'^$', views.home, name='home'),
]
