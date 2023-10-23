# Generated by Django 4.2.2 on 2023-10-23 03:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('tgl', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('nama', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.biodata')),
            ],
        ),
    ]
