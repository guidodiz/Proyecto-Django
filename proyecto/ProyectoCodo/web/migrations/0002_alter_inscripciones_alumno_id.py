# Generated by Django 5.0.6 on 2024-06-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripciones',
            name='alumno_id',
            field=models.ManyToManyField(blank=True, null=True, to='web.alumno'),
        ),
    ]