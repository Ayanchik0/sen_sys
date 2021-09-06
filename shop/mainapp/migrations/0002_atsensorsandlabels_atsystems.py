# Generated by Django 3.1.6 on 2021-08-31 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATsystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('technology', models.CharField(max_length=255, verbose_name='Технология')),
                ('sensor_detection_distance', models.CharField(max_length=255, verbose_name='Расстояние детекции датчиков')),
                ('tag_detection_distance', models.CharField(max_length=255, verbose_name='Расстояние детекции меток')),
                ('operating_frequency', models.CharField(max_length=255, verbose_name='Рабочая частота')),
                ('alarm_indication', models.CharField(max_length=255, verbose_name='Индикация тревоги')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ATsensorsandlabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('type', models.CharField(max_length=255, verbose_name='Тип')),
                ('technology', models.CharField(max_length=255, verbose_name='Технология')),
                ('of_availability', models.BooleanField(default=True)),
                ('operating_frequency', models.CharField(max_length=255, verbose_name='Рабочая частота')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]