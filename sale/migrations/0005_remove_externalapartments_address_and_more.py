# Generated by Django 5.0 on 2024-02-01 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_apartments_date'),
        ('sale', '0004_alter_externalapartments_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalapartments',
            name='address',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='date',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='description',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='id',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='price',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='show',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='sqft_living',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='status',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='the_developer',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='title',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='type',
        ),
        migrations.RemoveField(
            model_name='externalapartments',
            name='wall_material',
        ),
        migrations.AddField(
            model_name='externalapartments',
            name='apartments_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.apartments'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ExternalApartmentsImages',
        ),
    ]
