from django.shortcuts import render
from . import models
# Create your views here.

def show_model(request):
    data = models.contactModel.objects.all()
    return render(request, 'model.html', {'data': data})