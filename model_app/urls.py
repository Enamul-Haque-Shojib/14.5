
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('model/', views.show_model, name = 'model_page'),
]
