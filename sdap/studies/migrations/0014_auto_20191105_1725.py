# Generated by Django 2.2.5 on 2019-11-05 17:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0013_auto_20191031_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='expressiondata',
            name='cell_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expressiondata',
            name='class_name',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), default=list, size=None),
        ),
        migrations.AddField(
            model_name='expressiondata',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expressionstudy',
            name='species',
            field=models.CharField(choices=[('9606', 'Homo sapiens'), ('10090', 'Mus musculus'), ('10116', 'Rattus norvegicus'), ('9913', 'Bos taurus'), ('9544', 'Macaca mulatta'), ('9823', 'Sus scrofa'), ('9031', 'Gallus gallus'), ('7955', 'Danio rerio')], default='9606', max_length=50),
        ),
    ]