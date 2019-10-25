from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.current, name='current'),
    path('extended', views.extended, name='extended'),
    path('current', views.current, name='current'),
    path('radar', views.radar, name='radar'),
    path('discussion',views.discussion, name='discussion'),
]