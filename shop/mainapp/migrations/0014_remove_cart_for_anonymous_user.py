# Generated by Django 3.1.7 on 2021-09-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210905_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='for_anonymous_user',
        ),
    ]
