# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 00:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_week', models.CharField(max_length=12)),
                ('order_date', models.DateField()),
                ('order_qty', models.IntegerField()),
                ('fulfill_qty', models.IntegerField()),
                ('production_date', models.DateField()),
                ('trailer_num', models.CharField(max_length=25)),
                ('port_of_loading', models.CharField(max_length=100)),
                ('port_of_unlading', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prod_code_supplier', models.IntegerField(primary_key=True, serialize=False)),
                ('item_supplier', models.CharField(max_length=75)),
                ('prod_code_sumitomo', models.IntegerField()),
                ('item_sumitomo', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=144)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pork01.Suppliers'),
        ),
        migrations.AddField(
            model_name='orders',
            name='prod_code_sumitomo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pork01.Products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pork01.Suppliers'),
        ),
    ]
