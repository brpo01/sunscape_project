# Generated by Django 2.2.6 on 2019-11-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_propertie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertie',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
    ]