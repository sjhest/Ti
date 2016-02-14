# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 16:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('TIapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=64)),
                ('category', models.ManyToManyField(to='TIapp.Category')),
                ('item', models.ManyToManyField(to='TIapp.Item')),
                ('type', models.ManyToManyField(to='TIapp.Type')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_user',
            field=models.ForeignKey(default=datetime.datetime(2016, 2, 3, 16, 17, 35, 103927, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='TIapp.Ti_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 2, 3, 16, 18, 4, 144990, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 16, 18, 7, 705128, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='assigned_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TIapp.Department'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]