# Generated by Django 3.1.3 on 2020-11-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201123_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume',
            field=models.CharField(max_length=255, null=True, verbose_name='Максимальный объем встраиваемой памяти'),
        ),
    ]
