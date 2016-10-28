from django.conf.urls import url
from . import auth_views, views, profile_views, order_views, search_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', auth_views.register, name='register'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^profile/$', profile_views.profile, name='profile'),
    url(r'^add_food$', profile_views.add_food, name='add_food'),
    url(r'^search$', search_views.search, name='search'),
    url(r'^online_orders$', order_views.online_order, name='online_order'),
    url(r'^online_orders/(\d{0,3})/$', order_views.online_order, name='online_order'),
    url(r'^offline_orders$', order_views.offline_order, name='offline_order'),
    url(r'^order_food$', order_views.order_food, name='order_food'),
    url(r'^edit_food/(\d{1,3})/$', profile_views.edit_food, name='edit_food'),
    url(r'^fetch_shop_items/(\d{1,3})/$', views.fetch_shop_items, name='fetch_shop_items'),
    url(r'^fetch_shop_profile/(\d{1,3})/$', views.fetch_shop_profile, name='fetch_shop_profile'),
    url(r'^$', views.home, name='home'),
]
