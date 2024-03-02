from datetime import datetime

from django.db import models


class TelegramBotUsers(models.Model):
    name = models.CharField('Имя', max_length=250)
    chat_id = models.IntegerField('ID', default=0)

    date = models.DateTimeField('Дата создания', default=datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь Telegram Bot'
        verbose_name_plural = 'Пользователи Telegram Bot'
