from django import forms
from django.shortcuts import render

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject")

class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)