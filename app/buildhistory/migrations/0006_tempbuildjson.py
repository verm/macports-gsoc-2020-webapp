# Generated by Django 3.0.9 on 2020-08-03 08:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildhistory', '0005_builder_natural_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempBuildJSON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
    ]
