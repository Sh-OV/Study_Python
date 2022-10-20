from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, CallbackContext, ContextTypes
import datetime

# Сделаем метод-обертку над командами:
path = 'Homework_9\Telegram_Bot_1\collect_info.csv'
def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open(path, 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now()},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()