from django.conf.urls import url
from . import views, context_processors

urlpatterns = [
    url(r'^$', context_processors.cart_detail, name='cart_detail'),
    url(r'^add_main/(?P<dishesfororder_id>\d+)/$', views.cart_add_main, name='cart_add_main'),
    url(r'^remove_main/(?P<dishesfororder_id>\d+)/$', views.cart_remove_main, name='cart_remove_main'),
]