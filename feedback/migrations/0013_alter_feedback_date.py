# Generated by Django 5.0 on 2024-06-09 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0012_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 19, 57, 41, 307561), verbose_name='Дата публикации'),
        ),
    ]