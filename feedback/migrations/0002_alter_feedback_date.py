# Generated by Django 5.0 on 2023-12-28 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 16, 36, 1, 376545), verbose_name='Дата публикации'),
        ),
    ]