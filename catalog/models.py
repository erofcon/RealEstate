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
    title = models.CharField('Название', max_length=500)
    description = models.TextField('Описание')
    status = models.CharField('Статус', choices=STATUS_CHOICES, max_length=50, default='for_sale')
    type = models.CharField('Тип недвижимости', choices=APARTMENT_TYPE, max_length=70, default='new_buildings')
    show = models.BooleanField('Показывать на сайте?', default=False)
    price = models.IntegerField('Цена', default=1)
    floor = models.IntegerField('Этаж', default=1)
    bedrooms = models.IntegerField('Колличество комнат', default=1)
    sqft_living = models.FloatField('Сколько квадратных метров', default=1)
    address = models.CharField('Адрес', max_length=500, default=None, blank=True, null=True)
    wall_material = models.CharField('Материал стен', max_length=500, default=None, blank=True, null=True)
    the_developer = models.CharField('Застройщик', max_length=500, default=None, blank=True, null=True)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    plan = models.ImageField('Планировка', upload_to='media/', blank=True)
    external = models.BooleanField('Создано внешними клиентами?', default=False)
    contacts = models.TextField('Контакты для связи', blank=True, null=True)
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
