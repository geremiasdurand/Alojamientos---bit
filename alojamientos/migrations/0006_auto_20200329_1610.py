# Generated by Django 3.0.3 on 2020-03-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0005_auto_20200320_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamiento',
            name='barrio',
            field=models.CharField(choices=[('AG', 'Aguada'), ('BS', 'Barrio Sur'), ('BU', 'Buceo'), ('CS', 'Carrasco'), ('CT', 'Centro'), ('CE', 'Cerro'), ('CV', 'Ciudad Vieja'), ('CN', 'Cordón'), ('CR', 'Capurro'), ('LU', 'La Unión'), ('MÑ', 'Maroñas'), ('PR', 'Parque Rodó'), ('PÑ', 'Peñarol'), ('PC', 'Pocitos'), ('PG', 'Punta Gorda'), ('O', 'Pocitos')], default='O', max_length=2),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='direccion',
            field=models.CharField(default='O', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alojamiento',
            name='titulo',
            field=models.CharField(max_length=25),
        ),
    ]
