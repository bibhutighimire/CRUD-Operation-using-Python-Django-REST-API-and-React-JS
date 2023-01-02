from django.contrib import admin
from django.urls import path, include
from auth_app import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('registerpage', views.registerpage, name='registerpage'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logoutpage', views.logoutpage, name='logoutpage'),
    path('individualreport', views.individualreport, name='individualreport'),

]