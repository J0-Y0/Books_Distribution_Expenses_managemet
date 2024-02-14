from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.book_management, name='books'),
    path('add_book', views.add_book, name='add_book'),

    path('editBook/<int:id>/', views.editBook, name='editBook'),
    path('deleteBook/<int:id>/', views.deleteBook, name='deleteBook'),

    

]