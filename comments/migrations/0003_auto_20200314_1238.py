# Generated by Django 3.0.4 on 2020-03-14 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200311_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 12, 38, 45, 987077)),
        ),
    ]
