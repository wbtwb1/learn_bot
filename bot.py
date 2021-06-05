
from handler import guess_number
import logging #импорт модуля, кот сообщает об ошибках
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handler import (greet_user, guess_number, send_cat_picture, user_coordinates, planet,
                     talk_to_me)
import bot_settings
import ephem
from datetime import date, datetime 

logging.basicConfig(filename='bot.log', level=logging.INFO) # название файла и уровень важности сообщения (debug - самый нижний уровень, info - информационные сообщения,warning - предупреждение/оповещение, error - серьезная ошибка)

# PROXY = {'proxy_url': bot_settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {'username': bot_settings.PROXY_USERNAME, 'password': bot_settings.PROXY_PASSWORD}}


def main ():
    mybot = Updater (bot_settings.API_KEY, use_context=True)
    # mybot = Updater (bot_settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #CommandHandler - обработчик команд, указываем на какую команду должен реагировать
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.regex('^(Cat photo)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Bot was launched")
    mybot.start_polling() #бот обращается в ТГ за обновлениями
    mybot.idle() #чтобы бот не останавливал работу
    

main()
if __name__ == "__main__": #если вызвали этот файл, написав python3 bot.py, то он будет вызван, если из этого файла что-то импортировали, то функция мэйн не будет вызвана, чтобы не сломать код
    main()

    


    

