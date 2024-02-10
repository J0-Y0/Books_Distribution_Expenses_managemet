from django.shortcuts import redirect, render
from .models import *
from .form import *

def home(request):
    return render(request,"home.html")
def book_management(request):
    form = Books_form()
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            form = Books_form()
        else:
            form = Books_form(request.POST)
    books = Books.objects.all()
    
    return render(request,'book_management.html',{"books":books})
def add_book(request):
    form = Books_form()
    message = ""
    if request.method == 'POST':
        form = Books_form(request.POST)

        if form.is_valid():
            book =  form.save( commit=False)
            book.modification_log = "zare |yosef |add"
            book.save()
            message = "Done,Record saved "
            form = Books_form()
        else:
            form = Books_form(request.POST)
            message = "unable to save please try again !"

    context = {
        "title":"Add Book",
        "form":form,
        "message":message
      
    }
    return render(request,'book_crud.html',context)


def editBook(request,id):
    book = Books.objects.get(pk = id)
    message = ""
    form = Books_form( instance=book)
    if request.method == 'POST':
        form = Books_form(request.POST, instance=book)
        if form.is_valid():
            book =  form.save( commit=False)
            book.modification_log ="negem ==="+ book.modification_log
            book.save()
            message = "Done,Record saved "
            form = Books_form()
            message = "Done,Record saved "
        else:
            form = Books_form(instance=book)
            message = "unable to save please try again !"

    context = {
        "title":"edit Book",
        "form":form,
        "message":message
      
    }
    return render(request,'book_crud.html',context)

def deleteBook(request,id):
    book = Books.objects.get(pk = id)
    print(book.id)
    form = Books_form(instance=book)
    message = ""
    if request.method == 'POST':
        form = Books_form(request.POST, instance=book)

        if form.is_valid():
            message = "Done,Record Deleted "

            book.delete()
            return redirect('books')  # Redirect to a success URL

        else:
            form = Books_form(instance=book)
            message = "unable to save please try again !"

    context = {
        "title":"Add Book",
        "form":form,
        "message":message
      
    }
    return render(request,'book_crud.html',context)
