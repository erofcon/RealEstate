from django.db import models

from catalog.models import Apartments


class ExternalApartments(Apartments):
    contacts = models.TextField('Контакты для связи')
    external = models.BooleanField('Создано внешними клиентами?', default=False)

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'
