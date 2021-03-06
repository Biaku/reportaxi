# Generated by Django 2.0.2 on 2018-03-04 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorTaxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'color_taxi',
            },
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('calificacion', models.PositiveSmallIntegerField()),
                ('comentario', models.CharField(max_length=255)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ColorTaxi')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'taxi',
            },
        ),
    ]
