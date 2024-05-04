from django.conf import settings
import telebot

from .models import TelegramBotUsers

bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """ Привет!\nЭто бот для администратора сайта "Агенство ИБП" """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


def send_message(message):
    try:
        users = TelegramBotUsers.objects.all()
        for user in users:
            try:
                bot.send_message(chat_id=user.chat_id, text=message)
            except Exception:
                pass

    except Exception:
        pass
