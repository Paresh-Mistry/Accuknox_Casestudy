from django.urls import path 
from . import views

urlpatterns = [
    path('home' ,  views.home , name='home' ),
    path('rectangle' ,  views.rect , name='rect' )
]
