# Generated by Django 3.0.4 on 2020-03-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0002_auto_20200326_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(max_length=200, null=True),
        ),
    ]