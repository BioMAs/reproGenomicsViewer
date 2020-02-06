# Generated by Django 2.2.5 on 2019-11-26 13:34

from django.db import migrations, models
import sdap.studies.models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0022_auto_20191126_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='expressiondata',
            name='technology',
            field=models.CharField(choices=[('RNA-Seq', 'RNA-Seq'), ('ATAC-Seq', 'ATAC-Seq'), ('scRNA-Seq', 'scRNA-Seq'), ('MeDIP-Seq', 'MeDIP-Seq'), ('MBD-Seq', 'MBD-Seq'), ('CAGE', 'CAGE'), ('HITS-CLIP', 'HITS-CLIP'), ('MNase-Seq', 'MNase-Seq'), ('DNase-Hypersensitivity', 'DNase-Hypersensitivity'), ('PolyA-Seq', 'PolyA-Seq'), ('hMeDIP-Seq', 'hMeDIP-Seq'), ('MRE-Seq', 'MRE-Seq'), ('CAP-Seq', 'CAP-Seq'), ('PAS-Seq', 'PAS-Seq'), ('RIP-Seq', 'RIP-Seq'), ('Microwell-Seq', 'Microwell-Seq'), ('ChIP-Seq', 'ChIP-Seq')], default='RNA-Seq', max_length=50),
        ),
        migrations.AlterField(
            model_name='expressiondata',
            name='file',
            field=models.FileField(upload_to=sdap.studies.models.get_upload_path),
        ),
    ]