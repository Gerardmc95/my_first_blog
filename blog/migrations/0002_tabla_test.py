# Generated by Django 2.2.8 on 2019-12-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columna_uno', models.CharField(max_length=200)),
                ('columna_dos', models.CharField(max_length=200)),
                ('columna_tres', models.CharField(max_length=200)),
                ('columna_cuatro', models.CharField(max_length=200)),
            ],
        ),
    ]
