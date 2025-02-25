from django.urls import path 
from . import views

urlpatterns = [
    path('/my_signal_handler1' ,  views.my_signal_handler1 , name='my_signal_handler1' ),
    path('/my_signal_handler2' ,  views.my_signal_handler2 , name='my_signal_handler2' ),
    path('/my_signal_handler3' ,  views.my_signal_handler3 , name='my_signal_handler3' )
]
