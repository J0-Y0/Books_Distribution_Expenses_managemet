from django.contrib import admin
from .models import *
class booksAdmin(admin.ModelAdmin):
     list_display = ('idNumber','title','subtitle','author','publisher','published_date','distribution_expense',"modification_log",'category')

class book_typeAdmin(admin.ModelAdmin):
     list_display =('type_name','modification_log')

class profileAdmin(admin.ModelAdmin):
     list_display  =('user','phone','avatar')

admin.site.register(Profile,profileAdmin)
admin.site.register(Books, booksAdmin)
admin.site.register(Book_type,book_typeAdmin)

