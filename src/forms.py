from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(label="Subject")