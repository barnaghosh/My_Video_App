# Generated by Django 3.2.5 on 2021-08-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0007_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
