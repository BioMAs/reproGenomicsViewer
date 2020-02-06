# Generated by Django 2.2.5 on 2019-12-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0027_expressionstudy_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='expressionstudy',
            name='authors',
            field=models.TextField(blank=True, default='', verbose_name='Authors'),
        ),
        migrations.AddField(
            model_name='expressionstudy',
            name='publish_date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]