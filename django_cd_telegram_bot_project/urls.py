from django.urls import path, include
from django import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('registration/', views.reg),
    path('login/', views.login),
]
