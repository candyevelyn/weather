from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('extended', views.extended, name='extended'),
    path('current', views.current, name='current'),
]