from glob import glob
import ephem
from random import choice
from utils import get_smile, main_keyboard, play_random_numbers
from datetime import date, datetime 

def greet_user (update, context): #update - инфа, кот пришла из ТГ, context - позволяет отдавать команды боты изнутри функции
    print ('/start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Hello, user {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    ) #словарь, emoji - ключ словаря

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(f"{user_text} {context.user_data['emoji']}",
        reply_markup=main_keyboard())  #отправляем пользователю его же сообщение   

def planet (update, context):
    print ('/planet')
    try:
        planet_text = update.message.text.split()[1]
        planet_name = getattr(ephem, planet_text)
        constellation = ephem.constellation(planet_name(datetime.today()))
        update.message.reply_text(constellation, reply_markup=main_keyboard())
    except (AttributeError):
        update.message.reply_text (f'Введите планету из списка: Mars, Uranus, Pluto, Jupiter, Neptune, Mercury, Venus')

def guess_number(update, context):
    print ('/guess')
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message, reply_markup=main_keyboard())

def send_cat_picture(update, context):
    cat_photos_list = (glob('images/cat*.jp*g')) #получаем список картинок
    cat_photo_filename = choice(cat_photos_list) #выбираем случайную
    chat_id = update.effective_chat.id #чтобы получить айди чата текущего пользователя
    context.bot.send_photo(chat_id=chat_id, photo = open(cat_photo_filename, 'rb'), reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"`Your location` {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )