# Generated by Django 3.2.22 on 2023-10-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_shop', '0006_project_teammate'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='filename',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='filename',
            field=models.CharField(max_length=64, null=True),
        ),
    ]