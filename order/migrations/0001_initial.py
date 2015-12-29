# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial', models.CharField(max_length=255)),
                ('used_date', models.DateTimeField(null=True)),
                ('is_used', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Bonus_Record',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BonusType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=45)),
                ('item', models.FloatField(default=0.0)),
                ('send_organization', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Bonus_Type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DriverExpection',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('gender', models.BooleanField(default=None)),
                ('talkative', models.BooleanField(default=None)),
                ('other', models.CharField(max_length=255)),
                ('speak_eng', models.BooleanField(default=None)),
            ],
            options={
                'db_table': 'Driver_Expection',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MovingRequire',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('floor', models.IntegerField(default=1)),
                ('elevator', models.BooleanField(default=None)),
            ],
            options={
                'db_table': 'Moving_Require',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('item_motor', models.IntegerField(default=0)),
                ('item_pet', models.IntegerField(default=0)),
                ('item_single_bed', models.IntegerField(default=0)),
                ('item_twin_bed', models.IntegerField(default=0)),
                ('item_bookcase', models.IntegerField(default=0)),
                ('item_cupboard', models.IntegerField(default=0)),
                ('item_table', models.IntegerField(default=0)),
                ('item_chair', models.IntegerField(default=0)),
                ('item_refrigerator', models.IntegerField(default=0)),
                ('item_sofa', models.IntegerField(default=0)),
                ('item_fragile', models.IntegerField(default=0)),
                ('item_Other', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Order_Detail',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('reservation_date', models.DateField(default=datetime.datetime.now)),
                ('reservation_time', models.TimeField(default=b'12:00')),
                ('time_needed_hr', models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('time_needed_min', models.IntegerField(default=0, choices=[(0, 0), (30, 30)])),
                ('departure', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('wage', models.IntegerField(default=0)),
                ('name', models.CharField(default=None, max_length=45)),
                ('email', models.EmailField(default=None, max_length=75)),
                ('cell_phone', models.CharField(default=None, max_length=11, validators=[django.core.validators.MinLengthValidator(10)])),
                ('birth_year', models.IntegerField(default=None, max_length=4, null=True, choices=[(1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('birth_month', models.IntegerField(default=None, max_length=2, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('birth_day', models.IntegerField(default=None, max_length=2, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)])),
                ('remarks', models.TextField(default=None, max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('confirmation_key', models.CharField(default=None, max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.datetime.now)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Order_Status',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reservation_date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='timeofaday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='schedule',
            name='reservation_time',
            field=models.ForeignKey(to='order.timeofaday'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bonusrecord',
            name='fk_bonus_type',
            field=models.ForeignKey(related_name='bonus', to='order.BonusType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bonusrecord',
            name='fk_group_info',
            field=models.ForeignKey(related_name='bonus_records', on_delete=django.db.models.deletion.SET_NULL, to='member.GroupInfo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bonusrecord',
            name='fk_user_info',
            field=models.ForeignKey(related_name='bonus_records', on_delete=django.db.models.deletion.SET_NULL, to='member.UserInfo', null=True),
            preserve_default=True,
        ),
    ]
