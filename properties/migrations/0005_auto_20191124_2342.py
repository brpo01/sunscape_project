# Generated by Django 2.2.6 on 2019-11-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_propertie_photo_6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertie',
            name='zipcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
