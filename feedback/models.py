from datetime import datetime

from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=250)
    email = models.EmailField('Email', max_length=250, blank=True)
    subject = models.TextField('Сообщение')
    date = models.DateTimeField('Дата публикации', default=datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
