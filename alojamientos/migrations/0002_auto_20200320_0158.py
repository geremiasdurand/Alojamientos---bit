# Generated by Django 3.0.3 on 2020-03-20 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alojamiento',
            old_name='autor_id',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='alojamiento_id',
            new_name='alojamiento',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='autor_id',
            new_name='autor',
        ),
    ]