# Generated by Django 5.0 on 2024-06-09 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegrambotusers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 19, 51, 9, 204448), verbose_name='Дата создания'),
        ),
    ]
