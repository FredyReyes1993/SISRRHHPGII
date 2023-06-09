# Generated by Django 4.1.7 on 2023-05-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('ID_EMP', models.AutoField(primary_key=True, serialize=False, verbose_name='ID_EMPLEADO')),
                ('FOTO', models.ImageField(blank=True, upload_to='photos/empleados')),
                ('TDOC', models.CharField(default='', max_length=15, null=True, verbose_name='TIPO_DOCUMENTO')),
                ('NDOC', models.CharField(default='', max_length=13, null=True, unique=True, verbose_name='DPI')),
                ('DDOC', models.CharField(default='', max_length=50, null=True, verbose_name='DEPTO_DPI')),
                ('MDOC', models.CharField(default='', max_length=50, null=True, verbose_name='MUN_DPI')),
                ('PNOM', models.CharField(default='', max_length=50, null=True, verbose_name='PRIMER_NOMBRE')),
                ('SNOM', models.CharField(default='', max_length=50, null=True, verbose_name='SEGUNDO_NOMBRE')),
                ('PAPE', models.CharField(default='', max_length=50, null=True, verbose_name='PRIMER_APELLIDO')),
                ('SAPE', models.CharField(default='', max_length=50, null=True, verbose_name='SEGUNDO_APELLIDO')),
                ('ACAS', models.CharField(default='', max_length=50, null=True, verbose_name='APELLIDO_CASADA')),
                ('GEN', models.CharField(default='', max_length=20, null=True, verbose_name='GENERO')),
                ('FNAC', models.CharField(default='', max_length=10, null=True, verbose_name='FECHA_NAC')),
                ('ECIVIL', models.CharField(default='', max_length=25, null=True, verbose_name='ESTADO_CIVIL')),
                ('NNAC', models.CharField(default='', max_length=50, null=True, verbose_name='NAC_NACIMIENTO')),
                ('DNAC', models.CharField(default='', max_length=50, null=True, verbose_name='DEPTO_NACIMIENTO')),
                ('MNAC', models.CharField(default='', max_length=50, null=True, verbose_name='MUN_NACIMIENTO')),
                ('FALTA', models.CharField(default='', max_length=10, null=True, verbose_name='FECHA_ALTA')),
                ('TCONT', models.CharField(default='', max_length=25, null=True, verbose_name='TIPO_CONTRATO')),
                ('FFINAL', models.CharField(default='', max_length=10, null=True, verbose_name='FECHA_FINAL')),
                ('DEMP', models.CharField(default='', max_length=250, null=True, verbose_name='DIRECCION')),
                ('ZONA', models.CharField(default='', max_length=10, null=True, verbose_name='ZONA')),
                ('DDOM', models.CharField(default='', max_length=50, null=True, verbose_name='DEPTO_DOM')),
                ('MDOM', models.CharField(default='', max_length=50, null=True, verbose_name='MUN_DOM')),
                ('TELCASA', models.CharField(default='', max_length=10, null=True, verbose_name='TEL_CASA')),
                ('CELCASA', models.CharField(default='', max_length=10, null=True, verbose_name='CEL_CASA')),
                ('EMAIL', models.CharField(default='', max_length=100, null=True, verbose_name='EMAIL')),
                ('NEDUC', models.CharField(default='', max_length=25, null=True, verbose_name='N_EDUC')),
                ('GRAC', models.CharField(default='', max_length=25, null=True, verbose_name='GRADO')),
                ('NOMCENTRO', models.CharField(default='', max_length=100, null=True, verbose_name='CENTRO')),
                ('OBSER', models.CharField(default='', max_length=250, null=True, verbose_name='OBSERVACIONES')),
                ('PAR_1', models.CharField(default='', max_length=10, null=True, verbose_name='PARENTESCO')),
                ('PNOM1', models.CharField(default='', max_length=50, null=True, verbose_name='P_NOMBRE')),
                ('PAPE1', models.CharField(default='', max_length=50, null=True, verbose_name='P_APELLIDO')),
                ('PDIRE1', models.CharField(default='', max_length=100, null=True, verbose_name='DIRECCION')),
                ('PTEL1', models.CharField(default='', max_length=10, null=True, verbose_name='TELEFONO')),
                ('PAR_2', models.CharField(default='', max_length=10, null=True, verbose_name='PARENTESCO')),
                ('PNOM2', models.CharField(default='', max_length=50, null=True, verbose_name='P_NOMBRE')),
                ('PAPE2', models.CharField(default='', max_length=50, null=True, verbose_name='P_APELLIDO')),
                ('PDIRE2', models.CharField(default='', max_length=100, null=True, verbose_name='DIRECCION')),
                ('PTEL2', models.CharField(default='', max_length=10, null=True, verbose_name='TELEFONO')),
                ('PAR_3', models.CharField(default='', max_length=10, null=True, verbose_name='PARENTESCO')),
                ('PNOM3', models.CharField(default='', max_length=50, null=True, verbose_name='P_NOMBRE')),
                ('PAPE3', models.CharField(default='', max_length=50, null=True, verbose_name='P_APELLIDO')),
                ('PDIRE3', models.CharField(default='', max_length=100, null=True, verbose_name='DIRECCION')),
                ('PTEL3', models.CharField(default='', max_length=10, null=True, verbose_name='TELEFONO')),
                ('NOSERPEN', models.CharField(default='', max_length=25, null=True, verbose_name='NO_SERIE_PENAL')),
                ('FEMPEN', models.CharField(default='', max_length=25, null=True, verbose_name='FECHA_EM_PENAL')),
                ('FVEPEN', models.CharField(default='', max_length=25, null=True, verbose_name='FECHA_VEN_PENAL')),
                ('NOSERPOL', models.CharField(default='', max_length=25, null=True, verbose_name='NO_SERIE')),
                ('FEMPOL', models.CharField(default='', max_length=25, null=True, verbose_name='FECHA_EM_POLICIAL')),
                ('FVEPOL', models.CharField(default='', max_length=25, null=True, verbose_name='FECHA_VEN_POLICIAL')),
                ('GRUPO', models.CharField(default='', max_length=25, null=True, verbose_name='GRUPO_POBLACIONAL')),
                ('COMLIN', models.CharField(default='', max_length=100, null=True, verbose_name='COM_LIN')),
                ('AIGSS', models.CharField(default='', max_length=15, null=True, verbose_name='A_IGSS')),
                ('ANIT', models.CharField(default='', max_length=15, null=True, verbose_name='A_NIT')),
                ('AIRTRA', models.CharField(default='', max_length=15, null=True, verbose_name='A_IRTA')),
                ('POFICIO', models.CharField(default='', max_length=50, null=True, verbose_name='P_OFICIO')),
                ('TEXPE', models.CharField(default='', max_length=50, null=True, verbose_name='T_EXPEDIENTE')),
                ('PEMPLE', models.CharField(default='', max_length=50, null=True, verbose_name='PUESTO')),
                ('TLIC', models.CharField(default='', max_length=2, null=True, verbose_name='TIPO_LICENCIA')),
                ('NOLIC', models.CharField(default='', max_length=15, null=True, verbose_name='NO_LIC')),
                ('FVLIC', models.CharField(default='', max_length=10, null=True, verbose_name='VENC_LICENCIA')),
                ('SBM', models.CharField(default='', max_length=15, null=True, verbose_name='BASE_MENSUAL')),
                ('BINC', models.CharField(default='', max_length=15, null=True, verbose_name='BONO_INC')),
                ('JORLAB', models.CharField(default='', max_length=50, null=True, verbose_name='JOR_LABORAL')),
                ('TIPAGO', models.CharField(default='', max_length=25, null=True, verbose_name='TIPO_PAGO')),
                ('ESTATUS', models.CharField(default='A', max_length=1, null=True, verbose_name='ESTADO')),
                ('MBAJA', models.CharField(default='', max_length=500, null=True, verbose_name='MOTIVO_DESPIDO')),
                ('FACTUAL', models.DateTimeField(auto_now=True, verbose_name='FECHA_ACTUAL')),
            ],
        ),
    ]
