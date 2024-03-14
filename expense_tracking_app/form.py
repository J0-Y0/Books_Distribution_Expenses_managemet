# import form class from django
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


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
            
class User_form(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {

            'password1' :forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password','type':'password'}),
            'username' :forms.TextInput( attrs={'class': 'form-control', 'placeholder':'UserName'}),
            'password2' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'re-type the Password','type':'password'}), 
            # e"groups":forms.Select(attrs={'required':'true', "class": "form-select mb-1" }),

        }
        # custom validation 
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords do not match")
            return password2
        def clean_username(self):
            username = self.cleaned_data.get('username')
            # Check if username has been changed
            if self.instance.username != username:
                # If changed, validate uniqueness
                if User.objects.filter(username=username).exists():
                    raise forms.ValidationError("A user----- with that username already exists.")
            return username
class Username_update_Form(UserChangeForm):

    class Meta:
        model = User
        fields = ['username']
        widgets = {

            'username' :forms.TextInput( attrs={'class': 'form-control', 'placeholder':'UserName'}),

        }

class Profile_form(forms.ModelForm):
    class Meta:
        # avatar = forms.ImageField(widget=forms.FileInput( attrs={'class': 'form-control-file'}))
        model = Profile
        fields = ['first_name','last_name','phone','email','avatar','user_group']
        widgets = {
            'first_name' :forms.TextInput( attrs={'class': 'form-control', 'placeholder':'First Name '}),
            'last_name' :forms.TextInput( attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'email' :forms.EmailInput( attrs={'class': 'form-control', 'placeholder':'Email'}),
            'phone' :forms.TextInput( attrs={'type':'tel' ,'class': 'form-control', 'placeholder':'Phone'}),
            'avatar':   forms.FileInput(attrs={"class": "form-control"}) ,
            "user_group":forms.Select(attrs={'required':'true', "class": "form-select mb-1" }),

        }

class Category_form(forms.ModelForm):
    class Meta:
        model= Book_type
        fields = ['type_name']
        widgets = {
            'type_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Ex,Data Science'})
        }