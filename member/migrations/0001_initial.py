# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('photo_url', models.ImageField(null=True, upload_to=b'upload/user_profile_photo/')),
                ('identification_number', models.CharField(max_length=10)),
                ('birth_year', models.IntegerField(default=None, max_length=4)),
                ('birth_month', models.IntegerField(default=None, max_length=2)),
                ('birth_day', models.IntegerField(default=None, max_length=2)),
                ('gender', models.BooleanField(default=None)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Driver_Info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FacebookAccount',
            fields=[
                ('uid', models.BigIntegerField(serialize=False, primary_key=True, db_column=b'UID')),
                ('token', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Facebook_Account',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('photo_url', models.ImageField(null=True, upload_to=b'upload/group_profile_photo/')),
                ('address', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Group_Info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IndustryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Industry_Category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberAccount',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('password', models.CharField(default=None, max_length=45)),
                ('cell_phone', models.CharField(max_length=11)),
                ('phone_sms_verification', models.BooleanField(default=False)),
                ('activation_key', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('key_expired', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Memebr_Account',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemebrType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Member_Type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('photo_url', models.ImageField(null=True, upload_to=b'upload/user_profile_photo/')),
                ('birth_year', models.IntegerField(default=None, max_length=4, null=True)),
                ('birth_month', models.IntegerField(default=None, max_length=2, null=True)),
                ('birth_day', models.IntegerField(default=None, max_length=2, null=True)),
                ('gender', models.BooleanField(default=None)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
                ('fk_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.MemberAccount')),
                ('fk_fb_account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.FacebookAccount')),
            ],
            options={
                'db_table': 'User_Info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VocationCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Vocation_Category',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='fk_vocation_type',
            field=models.ForeignKey(related_name='users', on_delete=django.db.models.deletion.SET_NULL, to='member.VocationCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='memberaccount',
            name='fk_member_type',
            field=models.ForeignKey(related_name='type_accounts', on_delete=django.db.models.deletion.SET_NULL, to='member.MemebrType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='fk_account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.MemberAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='fk_industry',
            field=models.ForeignKey(related_name='groups', on_delete=django.db.models.deletion.SET_NULL, to='member.IndustryCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driverinfo',
            name='fk_account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.MemberAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driverinfo',
            name='fk_fb_account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.FacebookAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driverinfo',
            name='fk_vocation_type',
            field=models.ForeignKey(related_name='drivers', on_delete=django.db.models.deletion.SET_NULL, to='member.VocationCategory', null=True),
            preserve_default=True,
        ),
    ]
