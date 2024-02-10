from django.db import models
    
class Book_type(models.Model):
    type_name =models.CharField(max_length = 500 ,unique =True)
    modification_log = models.CharField(max_length = 2000)

class Books(models.Model):
    idNumber =models.IntegerField(unique=True) 
    title = models.CharField(max_length =500 ,null = False)
    subtitle = models.CharField(max_length =500 ,null = False)
    author = models.CharField(max_length =100 ,null = False)
    publisher = models.CharField(max_length =500 ,null = False)
    published_date = models.DateField(max_length =1000 ,null = False)
    distribution_expense = models.DecimalField(null = False,max_digits=8,decimal_places = 2)
   
    modification_log = models.CharField(max_length = 2000)
    
    category = models.ForeignKey( Book_type,on_delete = models.PROTECT) 
    # modification log 
    # append:
    #    {date_time | edit/create | userName}

# class userProfile(models.Model):
#      # user = [username, password,email]
#      user_group = admin/user
#      modification_log = models.CharField(max_length = 2000)

    