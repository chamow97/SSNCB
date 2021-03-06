# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171021_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(default=-1)),
                ('choice', models.CharField(default='NA', max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='answers',
            name='hint',
        ),
        migrations.AddField(
            model_name='questions',
            name='is_solved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answers',
            name='correct_option',
            field=models.CharField(default='NA', max_length=2000),
        ),
    ]
