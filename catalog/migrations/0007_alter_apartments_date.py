# Generated by Django 5.0 on 2024-02-01 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_apartments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 18, 8, 615543), verbose_name='Дата публикации'),
        ),
    ]
