from datetime import datetime

from django.db import models

STATUS_CHOICES = (
    ('for_sale', 'на продаже'),
    ('sales', 'продано'),
)

APARTMENT_TYPE = (
    ('secondary', 'вторичная'),
    ('new_buildings', 'новостройки'),
)


class Apartments(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    status = models.CharField('Статус', choices=STATUS_CHOICES, max_length=50, default='for_sale')
    type = models.CharField('Тип недвижимости', choices=APARTMENT_TYPE, max_length=70, default='new_buildings')
    show = models.BooleanField('Показывать на сайте?', default=False)
    price = models.IntegerField('Цена', default=0)
    floor = models.IntegerField('Этаж', blank=True)
    bedrooms = models.IntegerField('Колличество комнат', default=0)
    sqft_living = models.FloatField('Сколько квадратных метров', default=0)
    address = models.CharField('Адрес', max_length=250, default='')
    wall_material = models.CharField('Материал стен', max_length=250, blank=True)
    the_developer = models.CharField('Застройщик', max_length=250, blank=True)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    plan = models.ImageField('Планировка', upload_to='media/', blank=True)

    date = models.DateTimeField('Дата публикации', default=datetime.now())

    def __str__(self):
        return self.title

    def first_image(self):
        return self.images.first()

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'


class Images(models.Model):
    apartment = models.ForeignKey(Apartments, default=None, on_delete=models.CASCADE, related_name="images", )
    image = models.ImageField('Изображение', upload_to='media/', blank=True)

    def __str__(self):
        return self.apartment.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'
