# Generated by Django 3.2.23 on 2023-12-19 04:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_rename_link_link_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Link',
            new_name='Logins',
        ),
        migrations.RenameField(
            model_name='logins',
            old_name='login',
            new_name='link',
        ),
    ]
