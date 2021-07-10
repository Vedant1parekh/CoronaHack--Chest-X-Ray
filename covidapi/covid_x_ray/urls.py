from django.contrib import admin
from django.urls import path
from covid_x_ray import views
urlpatterns = [
    path('', views.index),
    path('result/', views.result),
]
