import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
chat_id_main = os.getenv('chat_id_main')
chat_id_test = os.getenv('chat_id_test')
target_time = os.getenv('target_time')
url = os.getenv('url')
