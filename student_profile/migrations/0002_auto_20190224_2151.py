# Generated by Django 2.1.5 on 2019-02-24 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_profile_pic',
            new_name='profile_pic',
        ),
    ]
