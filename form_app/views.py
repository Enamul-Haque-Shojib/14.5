from django.shortcuts import render
from . forms import contactForm
# Create your views here.

def show_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            return render(request, 'form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, 'form.html', {'form': form})
