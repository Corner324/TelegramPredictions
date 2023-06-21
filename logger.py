import logging
import asyncio
import config
import os
from datetime import datetime
from aiogram.types import InputFile
from aiogram import Bot, Dispatcher, executor, types 


class Logger:
    message_success = ''
    message_warn = ''
    bot = None
    
    def __init__(self, bot):
        logging.basicConfig(level=logging.INFO, filename="debug.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")
        
        self.bot = bot
        self.message_warn = f'[WARN] %s | {datetime.now()}'
        self.message_success = f'[SUCCESS] Message sends | {datetime.now()}'


    async def send_info_message(self, mes=None):
        if mes:
            logging.info(mes) 
            await self.bot.send_message(config.chat_id_test, mes)
            self.logging_in_file(mes)
        else:
            logging.info(self.message_success) 
            await self.bot.send_message(config.chat_id_test, self.message_success)
            self.logging_in_file(self.message_success)
        
            
    def warning_info(self, info_about_error = ''):
        logging.warning(self.message_warn % info_about_error, exc_info=True)
        self.logging_in_file(self.message_warn % info_about_error )


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
            

    def logging_in_file(self, text):
        pass
        # Except 'charmap' codec can't encode character
        # with open('log.txt','w') as file:
        #     file.write(text + '\n')        
