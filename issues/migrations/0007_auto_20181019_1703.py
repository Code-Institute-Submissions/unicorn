# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_auto_20181019_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='feature',
            field=models.CharField(choices=[('BUG', 'BUG'), ('FEATURE', 'FEATURE')], default='BUG', max_length=7),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('TODO', 'TODO'), ('DOING', 'DOING'), ('DONE', 'DONE')], default='TODO', max_length=5),
        ),
    ]