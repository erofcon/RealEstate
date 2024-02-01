from datetime import datetime

from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=250)
    contacts = models.TextField('Контакты для связи')
    subject = models.TextField('Сообщение')
    date = models.DateTimeField('Дата публикации', default=datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
