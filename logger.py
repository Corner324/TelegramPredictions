import logging
import asyncio
import config
import os

from datetime import datetime
from aiogram.types import InputFile


class Logger:
    message_success : str
    message_warn : str
    bot = None
    
    
    def __init__(self, bot):
        logging.basicConfig(level=logging.INFO, filename="debug.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
        
        self.bot = bot
        self.message_warn = f'[WARN] %s | {datetime.now()}'
        self.message_success = f'[SUCCESS] Message sends | {datetime.now()}'


    async def send_info_message(self, mes=None, timer=False):
        if mes:
            if not timer:
                await self.bot.send_message(config.chat_id_test, mes)
            logging.info(mes) 

        else:
            await self.bot.send_message(config.chat_id_test, self.message_success)
            logging.info(self.message_success) 

            
    def send_warning_message(self, info_about_error = ''):
        logging.warning(self.message_warn % info_about_error, exc_info=True)


    async def send_logs(self, bot, mess=None):
        current_time = str(datetime.now().time())
        
        try:
            with open('debug.log', 'r') as file:
                data = file.read()
                
            with open('logs.txt', 'w') as file:
                file.write(data)
            
            file_path = os.path.abspath('logs.txt')
            identif = config.chat_id_test
            if mess:
                identif = mess.from_user.id  
            
            await bot.send_document(chat_id = identif, document = InputFile(file_path), caption = f'Date: {current_time[:10]}')
        
        except Exception as Ex:
            await bot.send_message(config.chat_id_test, f'Could not read or write the file:\n{Ex}')
