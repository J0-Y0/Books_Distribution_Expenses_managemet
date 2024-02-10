from django.shortcuts import render
from .models import *

def home(request):
    return render(request,"home.html")
def book_management(request):
    books = Books.objects.all()
    return render(request,'book_management.html',{"books":books})
