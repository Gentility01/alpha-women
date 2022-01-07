from django import forms
from .models import ContactForm
from django.db import models
from django.forms import widgets
from django.forms.widgets import TextInput, Textarea
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Post


# class CreatePostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['image','title', 'cotent']


class MyContactForm(forms.Form):
    first_name = forms.CharField( max_length=50,
            widget=forms.TextInput(attrs={'id':'name','placeholder':'First name'}))
    last_name = forms.CharField( max_length=50,
            widget=forms.TextInput(attrs={'id':'surname','placeholder':'Surname'}))     
    email = forms.EmailField(
            widget=forms.EmailInput(attrs={'id':'email','placeholder':'Your email'}))
    
    male = forms.BooleanField( required=False,
            widget=forms.CheckboxInput(attrs={'name':'option1'}))
     
    female = forms.BooleanField( required=False,
            widget=forms.CheckboxInput(attrs={'name':'option2'}))
    
    message = forms.CharField(
            widget=forms.Textarea(attrs={'class':'form-control','placeholder':' Message'}))
    
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = ('first_name', 'last_name', 'email', 'message', 'male', 'female')

#     def __int__(self, *args, **kwargs):

