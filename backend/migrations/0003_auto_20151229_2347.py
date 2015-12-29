# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_backendimage'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='backendimage',
            table='back_Img',
        ),
    ]
