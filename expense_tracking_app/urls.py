from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.book_management, name='books'),
    path('add_book', views.add_book, name='add_book'),
    path('editBook/<int:id>/', views.editBook, name='editBook'),
    path('deleteBook/<int:id>/', views.deleteBook, name='deleteBook'),


    path('users', views.user_managment, name = 'users' ),
    path('add_user', views.add_user, name='add_user'),
    path('add_book', views.add_book, name='add_book'),
    path('editUser/<int:id>/', views.editUser, name='editUser'),
    path('deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),


    path('profile', views.my_profile, name='profile'),


    path('login', views.user_login, name = 'login' ),
    path('logout', views.user_logout, name = 'logout' ),
    path('reset', views.reset_password,name = "reset"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
