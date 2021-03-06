# Generated by Django 3.1.7 on 2021-09-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210904_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anti_theft_sensors_and_labels',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='anti_theft_systems',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='digital_automation',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='electronic_shelf_labels',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='key_pullers_and_deactivators',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ready_made_kits',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='shelving_protection',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='visitor_counter',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
    ]
