# Generated by Django 2.1.7 on 2019-08-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ports', '0006_add_clt_version_and_variants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='clt_version',
            field=models.CharField(default='', max_length=100),
        ),
    ]
