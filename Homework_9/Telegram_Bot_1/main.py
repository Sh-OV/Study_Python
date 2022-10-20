from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5539755775:AAE946jOvDqU1kmWTzQSFQRtBhjpF-l2ugQ").build()

print('server start')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("url", sslk))
app.add_handler(CommandHandler("phone", phone_command))

app.run_polling()