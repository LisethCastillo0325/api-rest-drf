# Generated by Django 3.2.7 on 2021-09-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_date',
            field=models.DateField(null=True, verbose_name='Fecha Finalización'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_finalized',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
