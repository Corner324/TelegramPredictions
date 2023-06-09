import logging
import config
import asyncio
import prediction
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime, time

'''
TODO: 
1) Проверить event_handler на  время
2) Написать парсер для предсказания
'''

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

logging.basicConfig(level=logging.INFO)
TOKEN = config.token
bot = Bot(token=TOKEN)
dispatch = Dispatcher(bot=bot)

@dispatch.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    usern_full_name = message.from_user.full_name
    logging.info(f'{user_id} | {usern_full_name} | {datetime.now()}')
    logging.info(message.chat.id)
    # await message.reply(datetime.now().strftime("%H:%M"))
    predict = get_full_predict()
    await bot.send_message(config.chat_id, predict)

async def event_handler():
    current_time = datetime.now().time()
    target_time = time(18, 0)  # Укажите желаемое время события
    if current_time >= target_time:
        data = prediction.parsing_horo()
        await bot.send_message(config.chat_id, str(data))
        

async def schedule_events():
    while True:
        await event_handler()
        await asyncio.sleep(60)  # Проверяем каждую минуту

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_events())
    executor.start_polling(dispatch, loop=loop)
