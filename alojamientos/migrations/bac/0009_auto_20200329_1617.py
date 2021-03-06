# Generated by Django 3.0.3 on 2020-03-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0008_auto_20200329_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamiento',
            name='telefono',
            field=models.DecimalField(decimal_places=0, default='Sin número de contacto', max_digits=15),
        ),
        migrations.AlterField(
            model_name='alojamiento',
            name='direccion',
            field=models.CharField(default='Sin dirección', max_length=50),
        ),
    ]
