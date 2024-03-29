# Generated by Django 4.2.7 on 2024-03-10 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('expense_tracking_app', '0011_remove_profile_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.group'),
            preserve_default=False,
        ),
    ]
