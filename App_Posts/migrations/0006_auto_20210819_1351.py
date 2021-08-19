# Generated by Django 3.2.5 on 2021-08-19 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0005_remove_post_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
