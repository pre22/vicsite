from django.core.mail import send_mail
from django import forms

class PasswordForm(forms.Form):
    usermail = forms.EmailField(max_length=50)