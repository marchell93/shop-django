# Generated by Django 3.1.3 on 2020-11-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20201123_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраиваемой памяти'),
        ),
    ]
