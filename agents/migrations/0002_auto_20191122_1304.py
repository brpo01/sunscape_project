# Generated by Django 2.2.6 on 2019-11-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
