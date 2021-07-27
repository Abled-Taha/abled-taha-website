from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from datetime import datetime
from . import emailSender

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            time = datetime.now()
            message_text = f'Someone wants to contact you. \n Email: {email} \n Subject: {subject} \n Time: {time}'
            emailSender.send(message_text)
            

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