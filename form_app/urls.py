
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_form, name = 'form_page'),
]
