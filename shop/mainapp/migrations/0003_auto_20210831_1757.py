# Generated by Django 3.1.6 on 2021-08-31 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_atsensorsandlabels_atsystems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ATsensorsandlabels',
            new_name='At_sensorsandlabels',
        ),
        migrations.RenameModel(
            old_name='ATsystems',
            new_name='At_systems',
        ),
    ]