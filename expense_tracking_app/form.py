# import form class from django
from django import forms
from .models import *

class Books_form(forms.ModelForm):
    # idNumber =forms.IntegerField(unique=True) 
    # title = forms.CharField(max_length =500 ,null = False)
    # subtitle = forms.CharField(max_length =500 ,null = False)
    # author = forms.CharField(max_length =100 ,null = False)
    # publisher = forms.CharField(max_length =500 ,null = False)
    # published_date = forms.DateField(widget=forms.DateField ,null = False)
    # distribution_expense = forms.DecimalField(null = False,max_digits=8,decimal_places = 2)
   
    # modification_log = forms.CharField(max_length = 2000)
    
    # category = forms.ForeignKey( Book_type,on_delete = models.PROTECT) 
 
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