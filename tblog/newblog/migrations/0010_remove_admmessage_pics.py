# Generated by Django 3.1.1 on 2021-03-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0009_auto_20201023_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admmessage',
            name='pics',
        ),
    ]
