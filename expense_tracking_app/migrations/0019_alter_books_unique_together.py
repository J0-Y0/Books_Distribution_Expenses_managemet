# Generated by Django 4.2.7 on 2024-03-12 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracking_app', '0018_alter_books_idnumber'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='books',
            unique_together={('idNumber', 'title', 'author')},
        ),
    ]
