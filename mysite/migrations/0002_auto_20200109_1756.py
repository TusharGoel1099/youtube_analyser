# Generated by Django 3.0 on 2020-01-09 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='llname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='name',
            old_name='name',
            new_name='lname',
        ),
    ]
