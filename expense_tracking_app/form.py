# import form class from django
from django import forms
from .models import *

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