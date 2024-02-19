# import form class from django
from django import forms
from .models import *
from django.contrib.auth.models import User

class Books_form(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ["modification_log"]
        widgets = {
                    "idNumber":forms.NumberInput(attrs={"class": "form-control mb-1","type":"number" }),
                    "title":forms.TextInput(attrs={"class": "form-control mb-1","type":"text"}),
                    "subtitle":forms.TextInput(attrs={"class": "form-control mb-1","type":"text"}),
                    "author":forms.TextInput(attrs={"class": "form-control mb-1","type":"text"}),
                    "publisher":forms.TextInput(attrs={"class": "form-control mb-1","type":"text"}),
                    "published_date":forms.DateInput(attrs={"class": "form-control mb-1","type":"date"}),
                    "distribution_expense":forms.NumberInput(attrs={"class": "form-control mb-1","type":"number"}),
                    "category":forms.Select(attrs={"class": "form-select mb-1" }),
                }
                
class User_form(forms.ModelForm):
    username = forms.CharField(  widget=forms.TextInput(attrs={'requred' 'class': 'form-control'})),
    email = forms.EmailField(required = True ,widget=forms.EmailInput(attrs={'class': 'form-control'}) ),
    password1 = forms.CharField(required = True ,widget=forms.PasswordInput(attrs={'class': 'form-control'}) ),
    password2 = forms.CharField(required = True ,widget=forms.PasswordInput(attrs={'class': 'form-control'}) ),
    # custom validation 
    class Meta:
        Model = User
        fields = ['username','email','password1','password2']
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords do not match")
            return password2

class Profile_form():
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    phone = forms.CharField(widget=forms.TextInput (attrs={'type':'tel','class': 'form-control'})),
    class Meta:
        Model = User
        fields = ['phone','avatar']
