# Generated by Django 4.1.7 on 2023-05-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ID_CLIENTES', models.AutoField(primary_key=True, serialize=False, verbose_name='ID_CLIENTE')),
                ('NOMBRE_CLIENTES', models.CharField(default='', max_length=150, verbose_name='NOMBRE_CLIENTE')),
                ('TELEFONO', models.CharField(default='', max_length=10, verbose_name='TELEFONO')),
                ('NIT', models.CharField(default='', max_length=15, verbose_name='NIT')),
                ('EMAIL_CLIENTE', models.CharField(default='', max_length=100, null=True, verbose_name='EMAIL')),
                ('DIRECCION_CLIENTE', models.CharField(default='', max_length=200, verbose_name='DIRECCION')),
                ('ESTATUS', models.CharField(default='A', max_length=1, verbose_name='ESTADO')),
                ('FECHA_ALTA', models.DateTimeField(auto_now_add=True, verbose_name='FECHA_ALTA')),
                ('FECHA_ACTUALIZACION', models.DateTimeField(auto_now=True, verbose_name='FECHA_ACTUALIZACION')),
            ],
            options={
                'db_table': 'CLIENTES',
            },
        ),
    ]
