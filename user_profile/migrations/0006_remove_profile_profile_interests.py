# Generated by Django 2.1.5 on 2019-04-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20190415_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_interests',
        ),
    ]