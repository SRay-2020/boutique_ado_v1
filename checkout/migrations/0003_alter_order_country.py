# Generated by Django 3.2.7 on 2021-09-16 11:10

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210916_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
