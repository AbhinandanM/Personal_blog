# Generated by Django 3.1.1 on 2020-09-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0007_admmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='img_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='img_category',
            field=models.CharField(default='', max_length=40),
        ),
    ]
