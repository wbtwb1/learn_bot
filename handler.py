from glob import glob
from random import choice
from utils import get_smile, main_keyboard, play_random_numbers, planet 

def greet_user (update, context): #update - инфа, кот пришла из ТГ, context - позволяет отдавать команды боты изнутри функции
    print ('Вызван /start')
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


def guess_number(update, context):
    print (context.args)
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
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = (choice(cat_photo_list))
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo = open(cat_photo_filename, 'rb'), reply_markup=main_keyboard())

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}!",
        reply_markup=main_keyboard()
    )