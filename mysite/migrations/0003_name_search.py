# Generated by Django 3.0 on 2020-01-09 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200109_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='search',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
