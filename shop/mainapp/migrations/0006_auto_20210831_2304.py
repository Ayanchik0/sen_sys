# Generated by Django 3.1.6 on 2021-08-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210831_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifrovaya_avtomatizacia_dlya_biznesa',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='datchiki_i_iteketki',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='electronnye_cenniki',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='gotovye_komplekty',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='kluchi_siemniki_i_deactivatory',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='protivokrazhsystemy',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='schetchiki_posetitelei',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='zashita_stelazhey',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Цена'),
        ),
    ]
