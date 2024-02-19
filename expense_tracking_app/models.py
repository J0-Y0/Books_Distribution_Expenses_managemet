from django.db import models
from django.contrib.auth.models import User

class Book_type(models.Model):
    type_name =models.CharField(max_length = 500 ,unique =True)
    modification_log = models.CharField(max_length = 2000)
    def __str__(self):
        return self.type_name

class Books(models.Model):
    idNumber =models.CharField(max_length = 600) 
    title = models.CharField(max_length =500 ,null = False)
    subtitle = models.CharField(max_length =500 ,null = True ,default ="")
    author = models.CharField(max_length =100 ,null = False)
    publisher = models.CharField(max_length =500 ,null = False)
    published_date = models.DateField( max_length =1000 ,null = False)
    distribution_expense = models.DecimalField(null = False,max_digits=8,decimal_places = 2)
   
    modification_log = models.CharField(max_length = 2000)
    
    category = models.ForeignKey( Book_type,on_delete = models.PROTECT) 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone  = models.CharField(max_length = 20)
    avatar = models.ImageField(default='default.jpg', upload_to='User_images')     



# modification log 
# append:
    #    {date_time | edit/create | userName}

# class userProfile(models.Model):
#      # user = [username, password,email]
#      user_group = admin/user
#      modification_log = models.CharField(max_length = 2000)

    