# Generated by Django 4.2.7 on 2024-02-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracking_app', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='User_images'),
        ),
    ]
