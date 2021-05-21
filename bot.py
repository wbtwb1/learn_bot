import logging #импорт модуля, кот сообщает об ошибках
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import bot_settings

logging.basicConfig(filename='bot.log', level=logging.INFO) # название файла и уровень важности сообщения (debug - самый нижний уровень, info - информационные сообщения,warning - предупреждение/оповещение, error - серьезная ошибка)

PROXY = {'proxy_url': bot_settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': bot_settings.PROXY_USERNAME, 'password': bot_settings.PROXY_PASSWORD}}

def greet_user (update, context): #update - инфа, кот пришла из ТГ, context - позволяет отдавать команды боты изнутри функции
    print ('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду/start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)  #отправляем пользователю его же сообщение   

def main ():
    mybot = Updater (bot_settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) #CommandHandler - обработчик команд, указываем на какую команду должен реагировать
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Запустился бот еее")
    mybot.start_polling() #бот обращается в ТГ за обновлениями
    mybot.idle() #чтобы бот не останавливал работу

    

main()
if __name__ == "__main__": #если вызвали этот файл, написав python3 bot.py, то он будет вызван, если из этого файла что-то импортировали, то функция мэйн не будет вызвана, чтобы не сломать код
    main()