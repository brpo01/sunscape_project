# Generated by Django 2.2.6 on 2019-11-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20191122_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertie',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]