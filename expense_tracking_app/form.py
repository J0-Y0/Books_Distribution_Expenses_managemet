# import form class from django
from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'
#     format='YYYY-MM-DD'
# # class EmailField(forms.EmailField):
# #     input_type = 'email'
# # create a ModelForm
class Books_form(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Books
        # widgets  = {
        #     'Year_Built': DateInput(),
        #     'SURVEY_Date':DateInput(),
        #     'Last_Retrofit':DateInput(),
        #     # 'Contact_Email':forms.EmailField(),
        #     # 'Contact_2_Email':forms.EmailField(),
            

            
        # }
        fields = "__all__"
