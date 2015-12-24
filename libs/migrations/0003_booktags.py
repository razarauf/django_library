# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0002_auto_20151218_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagname', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(to='libs.Book')),
            ],
        ),
    ]
