# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackAdmin',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('account', models.CharField(unique=True, max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('user_name', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Back_Admin',
            },
            bases=(models.Model,),
        ),
    ]
