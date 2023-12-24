from django.shortcuts import render
from .forms import ContactForm, AdminLoginForm
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
            r = requests.get(f"http://127.0.0.1:5000/225338242/create/{email}/{subject}")
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

def validateAdminLogin(username, password):
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False

def adminLogin(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            isDone = validateAdminLogin(username, password)
            if isDone:
                requestInfo = requests.get('http://127.0.0.1:5000/225338242/find').json()
                context = {
                    'title':    'AbledTaha | Admin',
                    'people':   requestInfo
                }
                return render(request, "admin.html", context)

    else:
        form = AdminLoginForm()
    context = {
        'title':    'AbledTaha | Admin Login',
        'form' :    form
    }
    return render(request, "adminLogin.html", context)