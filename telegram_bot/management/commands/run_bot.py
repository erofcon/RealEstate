from django.core.management.base import BaseCommand

from telegram_bot.main_bot import bot


class Command(BaseCommand):
    help = "Run Telegram Bot"

    def handle(self, *args, **options):
        bot.infinity_polling()
