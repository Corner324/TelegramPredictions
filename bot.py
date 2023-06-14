import logger
import config
import asyncio
import prediction
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
7) [T] Быстрая разверстка на сервере
'''

logger = logger.Logger()
TOKEN = config.token
bot = Bot(token=TOKEN)
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


@dispatch.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    #predict = get_full_predict()
    await bot.send_message(config.chat_id_test, 'Тестовый чат')

        
async def event_handler():
    
    minu = optimize_minute()
    current_time = str(datetime.now().time().hour) + ':' +  minu
    if current_time == config.target_time:
        predict = get_full_predict()
        
        if not predict:
            logger.warning_info()
            return 0
            
        ttime.sleep(60)
        logger.send_info_message()
        await bot.send_message(config.chat_id_main, predict)
        

async def schedule_events():
    while True:
        await event_handler()
        await asyncio.sleep(30) 


if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_events())
    executor.start_polling(dispatch, loop=loop, skip_updates=False)
