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
1) [T] Исправить ошибки покрытием
2) [ ] Пересмотреть архитектуру
3) [ ] 
4) [ ] 
5) [ ] 
'''

TOKEN = config.token
bot = Bot(token=TOKEN)
logger = logger.Logger(bot)
dispatch = Dispatcher(bot=bot)


def optimize_date(date):

    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    _, month, day = date.split('-')
    if str(day)[0] == '0':
        day = str(day).replace('0','')
        
    return f'{day} {months[int(month) - 1]}'

def get_hours():
    return str(datetime.now().time().hour)


def get_optimize_min():
    if len(str(datetime.now().time().minute)) == 1:
        minu = '0' + str(datetime.now().time().minute)
    else:
        minu = str(datetime.now().time().minute)
        
    return minu


def get_full_predict():
    date = datetime.today()
    date = str(date).split()[0]
    intro = optimize_date(date)

    data = prediction.parsing_horo()
    res = f'Прогноз на {intro} \n' + data
    return res


def is_actual_time():
    minu = get_optimize_min()
    current_time = str(datetime.now().time().hour) + ':' +  minu
    
    targer_hours, target_minut = config.target_time.split(':')
    
    if current_time == f'{targer_hours}:{target_minut}' or \
        current_time == f'{targer_hours}:{str((int(target_minut)+1))}' or \
        current_time == f'{targer_hours}:{str((int(target_minut)+2))}':
            return True


def debug_is_on():
    if sys.argv[1] == '-d':
        return True
    else:
        return False


@dispatch.message_handler(commands=['check'])
async def start_handler(message: types.Message):
    minu = get_optimize_min()
    hour = get_hours()
    current_time = f'{hour}:{minu}'

    res = f'Current time - {current_time}\n\
            Target time - {config.target_time}\n'
            
    await message.reply(res)
    await logger.send_logs(bot, message)
        

@dispatch.message_handler(commands=['logs'])
async def start_handler(message: types.Message):
    with open('log.txt','r') as file:
            data = file.read() 
    await bot.send_message(config.chat_id_test, data)

        
async def event_handler():
    
    minu = get_optimize_min()
    current_time = str(datetime.now().time().hour) + ':' +  minu
    if debug_is_on():
        # print('Target - ' + config.target_time)
        print('Current - ' + current_time)
        await logger.send_info_message(current_time, timer=True)
        
    if is_actual_time():
        predict = get_full_predict()
        
        if not predict:
            await logger.send_warning_message('Prediction miss')
            return 0
        
        await logger.send_info_message('Prediction posted!')
        await bot.send_message(config.chat_id_main, predict)
        ttime.sleep(190)
        

async def schedule_events():
    try:
        while True:
            await event_handler()
            await asyncio.sleep(15) 
    except Exception as Ex:
        logger.send_warning_message(f'While block\nP{Ex}')


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
        logger.send_warning_message('Main block: ' + str(e))
