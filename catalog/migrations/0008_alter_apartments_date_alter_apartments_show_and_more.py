# Generated by Django 5.0 on 2024-02-01 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_apartments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 27, 51, 926263), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='show',
            field=models.BooleanField(default=False, verbose_name='Показывать на сайте?'),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='type',
            field=models.CharField(choices=[('secondary', 'вторичная'), ('new_buildings', 'новостройки')], default='new_buildings', max_length=70, verbose_name='Тип недвижимости'),
        ),
    ]
