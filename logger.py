import logging
from datetime import datetime


class Logger:
    message_success = ''
    message_warn = ''
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        
        self.message_warn = f'[WARN] %s | {datetime.now()}'
        self.message_success = f'[SUCCESS] Message sends | {datetime.now()}'


    def send_info_message(self):
        logging.info(self.message_success)
        self.logging_in_file(self.message_success)
        
            
    def warning_info(self, info_about_error = ''):
        logging.info(self.message_warn % info_about_error)
        self.logging_in_file(self.message_warn % info_about_error )


    def logging_in_file(self, text):
        with open('log.txt','w') as file:
            file.write(text + '\n')        
