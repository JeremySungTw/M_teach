# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-11 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='訂製名稱')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='菜名')),
                ('price', models.IntegerField(verbose_name='價格')),
                ('info', models.CharField(blank=True, max_length=255, null=True, verbose_name='詳細資訊')),
                ('custom', models.ManyToManyField(blank=True, null=True, to='app01.Custom', verbose_name='客製化')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.CharField(max_length=255, verbose_name='發起人')),
                ('release_date', models.DateField(verbose_name='訂購日期')),
                ('deadline_date', models.DateField(blank=True, null=True, verbose_name='截止日期')),
                ('info', models.CharField(blank=True, max_length=255, null=True, verbose_name='訂單備註')),
            ],
        ),
        migrations.CreateModel(
            name='Orderdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderer', models.CharField(max_length=255, verbose_name='訂購人')),
                ('quantity', models.IntegerField(verbose_name='餐點數量')),
                ('info', models.CharField(blank=True, max_length=255, null=True, verbose_name='餐點備註')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='店名')),
                ('phone', models.CharField(max_length=255, verbose_name='電話')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='地址')),
                ('delivery', models.PositiveIntegerField(blank=True, null=True, verbose_name='外送金額')),
                ('menu_pic', models.CharField(blank=True, max_length=255, null=True, verbose_name='菜單圖片')),
                ('eva', models.PositiveIntegerField(blank=True, null=True, verbose_name='評價')),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('black_list', models.BooleanField(default=False, verbose_name='黑名單')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='類型名稱')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='type',
            field=models.ManyToManyField(blank=True, to='app01.Type'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Shop'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menuName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Shop'),
        ),
    ]
