# Generated by Django 2.2.10 on 2020-05-01 11:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_version', models.CharField(max_length=10)),
                ('xcode_version', models.CharField(max_length=10)),
                ('os_arch', models.CharField(max_length=20)),
                ('build_arch', models.CharField(default='', max_length=20)),
                ('platform', models.CharField(default='', max_length=20)),
                ('macports_version', models.CharField(max_length=10)),
                ('cxx_stdlib', models.CharField(default='', max_length=20)),
                ('clt_version', models.CharField(default='', max_length=100)),
                ('raw_json', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('timestamp', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.UUID')),
            ],
            options={
                'verbose_name': 'Statistics Submission',
                'verbose_name_plural': 'Statistics Submissions',
                'db_table': 'submission',
            },
        ),
        migrations.CreateModel(
            name='PortInstallation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('variants', models.CharField(default='', max_length=200)),
                ('requested', models.BooleanField(default=False)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.Submission')),
            ],
            options={
                'verbose_name': 'Installed Port',
                'verbose_name_plural': 'Installed Ports',
                'db_table': 'installed_ports',
            },
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['timestamp'], name='submission_timesta_0ed555_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['user'], name='submission_user_id_dd4875_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['user', '-timestamp'], name='submission_user_id_fa4b00_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['user', 'timestamp'], name='submission_user_id_f4b6a3_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_version'], name='submission_os_vers_5fb150_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_version', 'os_arch'], name='submission_os_vers_1bb250_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_version', 'xcode_version'], name='submission_os_vers_a02781_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['os_arch'], name='submission_os_arch_ebd5c3_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['macports_version'], name='submission_macport_071a1f_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['cxx_stdlib'], name='submission_cxx_std_de2798_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['build_arch'], name='submission_build_a_40018f_idx'),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['clt_version'], name='submission_clt_ver_5a7a78_idx'),
        ),
        migrations.AddIndex(
            model_name='portinstallation',
            index=models.Index(fields=['submission'], name='installed_p_submiss_b00f1e_idx'),
        ),
        migrations.AddIndex(
            model_name='portinstallation',
            index=models.Index(fields=['port'], name='installed_p_port_97f418_idx'),
        ),
        migrations.AddIndex(
            model_name='portinstallation',
            index=models.Index(fields=['variants'], name='installed_p_variant_789a6f_idx'),
        ),
    ]