# Generated by Django 2.1.2 on 2018-10-26 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12)),
                ('razon_social', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('comuna', models.CharField(max_length=255)),
                ('giro', models.CharField(max_length=255)),
            ],
        ),
    ]
