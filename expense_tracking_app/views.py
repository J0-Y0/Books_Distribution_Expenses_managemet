from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .form import *
from datetime import datetime
from openpyxl import load_workbook


def home(request):
    return render(request,"home.html")
def book_management(request):
    
    books_list = Books.objects.all()
    paginator = Paginator(books_list,4)
    page_num = request.GET.get('page',1)
    try:
        books = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        books = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        books = paginator.page(paginator.num_pages)

    
    return render(request,'book_management.html',{"books":books})
def add_book(request):
    form = Books_form()
    message = ""
    # add individually 
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



    # import from excel sheet
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']
        wb = load_workbook(excel_file)
        ws = wb.active

        try:
            for row in ws.iter_rows(min_row=2, values_only=True):
                id,title	,subtitle	,authors	,publisher,	published_date,	category,	distribution_expense = row
                category_typ = Book_type.objects.filter(type_name__exact = category.strip()).first()
                if category_typ == None:
                    modification_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" | "+str(request.user)+" | Imported"
                    Book_type.objects.create(type_name = category.strip(),modification_log = modification_log)
                modification_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S") +" | "+str(request.user)+" | Imported"
                Books.objects.create( idNumber =id,title =title	, subtitle =subtitle	,author =authors	, publisher =publisher,	published_date =published_date,	category=category_typ,	 distribution_expense =distribution_expense ,modification_log = modification_log)
            
            context = {"header":"Successfully Imported",
                        "message":"Imported Books:"}
            return render(request, 'success.html',context)
        except Exception as  e:
                context = {"header":"Unable to Import !!!",
                           "message":e}
                return render(request, 'success.html',context)
      
    context = {
        "title":"Add Book",
        "header":"Add Book | Adding a Record ",
        "description":"Add a book, fill out all the required field, and save. You can add multiple records as you wish, and you have the option to import records from an Excel sheet by clicking the import button.",
        "submitBtn":"Save,Add Another",
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
                    
            return redirect('books')  # Redirect to a success URL

        else:
            form = Books_form(instance=book)
            message = "unable to save please try again !"
    context = {
        "title":"Update Records",
        "header":"Update Records | Editing Books Data ",
        "description":"Edit book data effortlessly: simply modify the field data, save your changes, and watch as they're promptly updated in the database",
        "submitBtn":"Update",
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
        "title":"Delete Records",
        "header":"Delete | Erasing Books Data ",
        "description":"Erasing Books Data,Are you sure you want to delete this book? Deleting it is permanent, with no option for recovery once it's lost. If you're uncertain, please cancel the action",
        "submitBtn":"Delete ",
        "form":form,
        "message":message
      
    }
    return render(request,'book_crud.html',context)
