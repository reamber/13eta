# Generated by Django 2.1.5 on 2019-04-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_remove_profile_profile_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_perm_notify',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_perm_phone',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_perm_search',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_perm_view',
            field=models.BooleanField(default='True'),
        ),
    ]
