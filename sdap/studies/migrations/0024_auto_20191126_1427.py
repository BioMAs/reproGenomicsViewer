# Generated by Django 2.2.5 on 2019-11-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0023_auto_20191126_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='database',
            name='api_key',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
