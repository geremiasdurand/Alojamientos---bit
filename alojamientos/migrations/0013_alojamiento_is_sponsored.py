# Generated by Django 3.0.3 on 2020-04-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0012_auto_20200410_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamiento',
            name='is_sponsored',
            field=models.BooleanField(default=False),
        ),
    ]
