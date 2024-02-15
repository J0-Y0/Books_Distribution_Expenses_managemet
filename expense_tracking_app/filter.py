import django_filters
from .models import Books

class BookFilter(django_filters.FilterSet):
    idNumber =django_filters.NumberFilter(lookup_expr="gte",field_name="idNumber")
    title = django_filters.CharFilter(lookup_expr="icontains", field_name="title")
    author = django_filters.CharFilter(lookup_expr="icontains",field_name="author")
    publisher = django_filters.CharFilter(lookup_expr="icontains" ,field_name="publisher")
    published_date = django_filters.NumberFilter(lookup_expr="gte", field_name = "published_date")
    distribution_expense = django_filters.NumberFilter(lookup_expr = "gte", field_name="distribution_expense")
    category = django_filters.ChoiceFilter(field_name = "category", Lookup_expr="exact")
    class Meta:
        model = Books
        fields = ["idNumber","title","author","publisher","published_date","distribution_expense","category"]
    