from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton
import bot_settings


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(bot_settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли' 
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, ничья' 
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли' 
    return message 

def main_keyboard():
    return ReplyKeyboardMarkup([['Send me a cat', KeyboardButton('Мои координаты', request_location=True)]],resize_keyboard=True)  
