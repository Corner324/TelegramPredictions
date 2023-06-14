import logging
from datetime import datetime


class Logger:
    message_success = ''
    message_warn = ''
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        
        self.message_warn = f'ОШИБКА! | {datetime.now()}'
        self.message_success = f'Сообщение отправлено. | {datetime.now()}'


    def send_info_message(self):
        logging.info(self.message_success)
        self.logging_in_file(self.message_success)
        
            
    def warning_info(self):
        logging.info(self.message_warn)
        self.logging_in_file(self.message_warn)


    def logging_in_file(self, text):
        with open('log.txt','w') as file:
            file.write(text + '\n')        
