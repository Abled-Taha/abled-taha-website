from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from datetime import datetime

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            time = datetime.now()
            with open("contacts.txt", "a+") as File:
                File.write(f"{email}\n{subject}\n{time}\n\n")

    else:
        form = ContactForm()
    context = {
        'title':    'AbledTaha.us.to | Home',
        'form':     form
    }
    return render(request, "index.html", context)

def generic(request):
    context = {
        'title':    'AbledTaha.us.to | Generic'
    }
    return render(request, "generic.html", context)