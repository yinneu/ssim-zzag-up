# Generated by Django 3.2.22 on 2023-10-31 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_shop', '0007_auto_20231031_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='project',
            name='filename',
        ),
        migrations.AddField(
            model_name='boardimages',
            name='filename',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='projectimages',
            name='filename',
            field=models.CharField(max_length=64, null=True),
        ),
    ]