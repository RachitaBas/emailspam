from django import forms
from django.forms import ModelForm
from .models import Contact


class contact_form(ModelForm):
     class Meta:
         model=Contact
         fields=['first_name',
         'last_name',
         'email',
         'phone',
         'message',]



# class Contact(forms.Form):
#     First_name = forms.CharField(label='First name', max_length=100)
#     Last_name = forms.CharField(label='Last name', max_length=100)
#     Email = forms.CharField(label='Email', max_length=100)
#     phone = forms.CharField(label='Phone',)
#     Message = forms.CharField(label='Message', widget=forms.Textarea)