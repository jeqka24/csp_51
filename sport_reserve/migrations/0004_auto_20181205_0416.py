# Generated by Django 2.1.2 on 2018-12-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_reserve', '0003_auto_20181111_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='AssignedSportsmen',
            field=models.ManyToManyField(help_text='Назначенные спортсмены', to='sport_reserve.Sportsman', verbose_name='Назначенные спортсмены'),
        ),
        migrations.AddField(
            model_name='event',
            name='AssignedTrainers',
            field=models.ManyToManyField(help_text='Назначенный тренер', to='sport_reserve.Trainer', verbose_name='Назначенные тренеры'),
        ),
    ]