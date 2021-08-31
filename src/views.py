from django.shortcuts import render
from .forms import ContactForm
import requests

def error(request, exception):
    context = {
        "title" :       "Error - 404 | Page Not Found"
    }
    return render(request, "error.html", context)

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            r = requests.get(f"https://contact-me-api-python.herokuapp.com/225338242/create/{email}/{subject}")
            context = {
                'title' : 'AbledTaha | Done'
            }
            return render(request, 'done.html', context)

    else:
        form = ContactForm()
    context = {
        'title':    'AbledTaha | Home',
        'form':     form
    }
    return render(request, "index.html", context)

def secret(request):
    context = {
        'title':    'AbledTaha | Secret'
    }
    return render(request, "secret.html", context)