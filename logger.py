import logging
import asyncio
import config
from datetime import datetime


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


    def logging_in_file(self, text):
        pass
        # Except 'charmap' codec can't encode character
        # with open('log.txt','w') as file:
        #     file.write(text + '\n')        
