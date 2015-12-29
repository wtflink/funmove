# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPayment',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('card_number', models.CharField(max_length=16)),
                ('security_code', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Card_Payment',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditCardType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=45)),
                ('security_code_length', models.IntegerField()),
                ('card_length', models.IntegerField()),
                ('card_begin_number', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Credit_Card_Type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.CharField(max_length=45)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_admin', models.CharField(max_length=45)),
                ('update_admin', models.CharField(max_length=45)),
                ('deactivated_admin', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'Payment_Option',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentRecords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(null=True, blank=True)),
                ('deactivated', models.BooleanField(default=False)),
                ('create_account', models.CharField(max_length=45)),
                ('update_account', models.CharField(max_length=45)),
                ('deactivated_account', models.CharField(max_length=45, null=True, blank=True)),
                ('fk_group_info', models.ForeignKey(related_name='payment_records', on_delete=django.db.models.deletion.SET_NULL, to='member.GroupInfo', null=True)),
                ('fk_payment_option', models.ForeignKey(related_name='payment_records', to='payment.PaymentOption')),
                ('fk_user_info', models.ForeignKey(related_name='payment_records', on_delete=django.db.models.deletion.SET_NULL, to='member.UserInfo', null=True)),
            ],
            options={
                'db_table': 'Payment_Records',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cardpayment',
            name='fk_card_type',
            field=models.ForeignKey(related_name='card_payments', on_delete=django.db.models.deletion.SET_NULL, to='payment.CreditCardType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardpayment',
            name='fk_payment_record',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.PaymentRecords'),
            preserve_default=True,
        ),
    ]
