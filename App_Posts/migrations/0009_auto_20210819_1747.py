# Generated by Django 3.2.5 on 2021-08-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0008_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='post',
            name='catagory',
            field=models.CharField(max_length=100),
        ),
    ]