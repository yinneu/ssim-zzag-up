# Generated by Django 3.2.22 on 2023-11-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_shop', '0008_auto_20231031_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]