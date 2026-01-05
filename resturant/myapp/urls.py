from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('', views.user_login, name='login')
   
    
]