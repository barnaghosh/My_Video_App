# Generated by Django 3.2.5 on 2021-08-19 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0003_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
