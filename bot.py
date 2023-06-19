import logger
import config
import asyncio
import prediction
import sys
import time as ttime
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime, time


'''
TODO: 
1) [X]  Проверить event_handler на время
2) [X] Написать парсер для предсказания
3) [X] Найти хостинг под бота
4) [T] Создать логирование в файл
5) [T] Исправить ошибки покрытием
6) [ ] Пересмотреть архитектуру
7) [X] Быстрая разверстка на сервере
8) [X] Добавить функцию под Debug
9) [X] Добавить логирование отправки в тестовый чат
'''

TOKEN = config.token
bot = Bot(token=TOKEN)
logger = logger.Logger(bot)
dispatch = Dispatcher(bot=bot)


def transform_date(date):

    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    _, month, day = date.split('-')
    day = str(day).replace('0','')
    return f'{day} {months[int(month) - 1]}'


def get_full_predict():
    date = datetime.today()
    date = str(date).split()[0]
    intro = transform_date(date)

    data = prediction.parsing_horo()
    res = f'Прогноз на {intro} \n' + data
    return res


def optimize_minute():
    if len(str(datetime.now().time().minute)) == 1:
        minu = '0' + str(datetime.now().time().minute)
    else:
        minu = str(datetime.now().time().minute)
        
    return minu


def debug_is_on():
    if sys.argv[1] == '-d':
        return True
    else:
        return False


@dispatch.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    logger.send_info_message()
    logger.warning_info()
    #await bot.send_message(config.chat_id_test, 'Тестовый чат')


@dispatch.message_handler(commands=['check'])
async def start_handler(message: types.Message):
    minu = optimize_minute()
    current_time = str(datetime.now().time().hour) + ':' +  minu
    
    res = f'Current time - {current_time}\nTarget time - {config.target_time}\n'
    await message.reply(res)
    
    await logger.send_logs(bot)
        


@dispatch.message_handler(commands=['logs'])
async def start_handler(message: types.Message):
    with open('log.txt','r') as file:
            data = file.read() 
    await bot.send_message(config.chat_id_test, data)

        
async def event_handler():
    
    minu = optimize_minute()
    current_time = str(datetime.now().time().hour) + ':' +  minu
    if debug_is_on():
        # print('Target - ' + config.target_time)
        print('Current - ' + current_time)
        
    if current_time == config.target_time:
        predict = get_full_predict()
        
        if not predict:
            logger.warning_info('Prediction miss')
            return 0
        
        await logger.send_info_message()
        await bot.send_message(config.chat_id_main, predict)
        ttime.sleep(60)
        

async def schedule_events():
    try:
        while True:
            await event_handler()
            await asyncio.sleep(15) 
    except:
        logger.warning_info('While block')



async def on_startup(x):
    await logger.send_info_message('✅| Bot is Running')

async def on_shutdown(x):
    await logger.send_info_message('🆘| Bot is Shutdown!')
    await logger.send_logs(bot)


if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.create_task(schedule_events())
        executor.start_polling(dispatcher=dispatch,
                               skip_updates=True,
                               on_startup=on_startup,
                               on_shutdown=on_shutdown,
                               loop=loop)
    except Exception as e:
        logger.warning_info('Main block: ' + str(e))
