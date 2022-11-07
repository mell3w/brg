from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('menu',views.menu, name='menu'),
    path('',views.index, name='home'),
]