# Generated by Django 3.1.1 on 2020-10-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_content', '0002_videos_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to='media_root/videos/'),
        ),
    ]
