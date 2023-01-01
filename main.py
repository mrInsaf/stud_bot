from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import logging

# Настройка логирования
logging.basicConfig(level='INFO', filename='log.log')
logger = logging.getLogger()
logging.getLogger('apscheduler.scheduler').setLevel('CRITICAL')

# Настройка бота
updater = Updater(token='5890920382:AAHnywZK-FlmBbU3bbD7DTfC4IH_8QbPwgs')

# Словарь с названиями месяцев
months = {1:'Января', 2:'Феваля', 3:'Марта', 4:'Апреля', 5:'Мая', 6:'Июня', 7:'Июля', 8:'Августа', 9:'Сенября',
          10:'Октября', 11:'Ноября', 12:'Декабря'}


def send_report_to_me(text):
    chat_id = 816831722
    updater.bot.send_message(chat_id, text)

def create_pic(path):
    image = Image.open(path)
    font = ImageFont.truetype("C:\Windows\Fonts\Century.ttf", 70)
    drawer = ImageDraw.Draw(image)
    current_datetime = datetime.today()
    drawer.text((50, 100), f'Сегодня\n{current_datetime.day} {str.lower(months[current_datetime.month])} \n\n '
                           f'Время\n {current_datetime.hour}:{f"{current_datetime.minute:02}"}', font=font, fill='#373737')
    image.save('new_img.jpg')


def start(update, context):
    log_text = f'Date request from {update.message.from_user.username} at {update.message.date}'
    logger.info(log_text)
    send_report_to_me(log_text)
    chat = update.effective_chat
    create_pic("teb-full.jpg")
    updater.bot.send_photo(chat_id=chat.id, photo=open('new_img.jpg', 'rb'))


def other_requests(update, context):
    log_text = f'Other request from {update.message.from_user.username} at {update.message.date}. Text: {update.message.text}'
    logger.info(log_text)
    send_report_to_me(log_text)
    update.message.reply_text('Я вас не понимаю :(')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, other_requests))
updater.start_polling()


