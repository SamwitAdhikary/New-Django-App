# Generated by Django 3.1.7 on 2021-03-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default=models.CharField(default='', max_length=100), max_length=100),
        ),
    ]
