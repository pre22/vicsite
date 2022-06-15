from django import forms
from django.http import request
from accounts.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact 
        fields =["c_email", "msg",]
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields["c_email"].widget.attrs.update({"class": "block w-full border border-gray-200 rounded-md py-2 px-4 mt-2", "type": "email", "placeholder": "Enter your email address here"})

        self.fields["msg"].widget.attrs.update({"class": "block w-full border border-gray-200 rounded-md py-2 px-4 mt-2", "type": "text"})


    def save(self, request):
        self.c_email = self.cleaned_data['c_email']
        self.msg = self.cleaned_data['msg']
        super(ContactForm, self).save(request)
