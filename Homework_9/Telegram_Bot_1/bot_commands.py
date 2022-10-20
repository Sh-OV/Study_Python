from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from pytube import YouTube 

# from Homework_9.Telephone_directory.view_gen import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}! \
        Поделшься со мной своим телефоном? (Введите /ok или /no) :-)')
    await update.message.reply_text(f'/ok\n/no')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/url\n/phone')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()      # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
    
async def sslk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Bcтавьтe ссылку для скачивания') 
    url = update.message.text 
    print(url) 
    yt = YouTube(url) 
    yt. streams. filter(progressive= True) 
    yt. streams. filter(only_audio=True) 
    print(yt.streams) 


async def phone_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Поделись со мной своим номером телефона? :-)')
    name = update.effective_user.first_name
    
    phone = update.message.text 
    # print(f'answer = {answer}')
    print(f'name = {name}')
    print(f'phone = {phone}')
    return name, phone
    
    
    