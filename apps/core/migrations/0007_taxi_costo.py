# Generated by Django 2.0.2 on 2018-03-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180309_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxi',
            name='costo',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
