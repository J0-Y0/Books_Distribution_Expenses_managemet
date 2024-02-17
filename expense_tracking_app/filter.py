import django_filters
from .models import Books,Book_type
from django.forms.widgets import TextInput,DateInput,ChoiceWidget,NumberInput,Select


class BookFilter(django_filters.FilterSet):
    idNumber =django_filters.CharFilter(lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'Id number','class':"form-control "}))
    title = django_filters.CharFilter(lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Title','class':"form-control"}))
    author = django_filters.CharFilter(lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Author','class':"form-control"}))
    publisher = django_filters.CharFilter(lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Publisher','class':"form-control"}))
    published_date = django_filters.DateFilter(lookup_expr='gt',widget=DateInput(attrs={'placeholder': 'published date',"pattern":"\d{2}-\m{2}-\y{4}", "format" :'dd-mm-yyyy' , 'type':'date','class':"form-control"}))
    distribution_expense = django_filters.NumberFilter(widget=NumberInput(attrs={'placeholder': 'Distribution Expense','class':"form-control"}))
    category = django_filters.ModelChoiceFilter(queryset = Book_type.objects.all(), widget=Select(attrs={'placeholder': 'Distxpense','class':"    form-select"}))
    class Meta:
        model = Books
        fields = ["idNumber","title","author","publisher","published_date","distribution_expense","category"]
