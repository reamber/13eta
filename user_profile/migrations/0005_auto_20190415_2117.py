# Generated by Django 2.1.5 on 2019-04-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20190401_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_contact_info',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_education',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_email',
            field=models.CharField(default='no email provided', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_major',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_year',
            field=models.CharField(default='', max_length=100),
        ),
    ]