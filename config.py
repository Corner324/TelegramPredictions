import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
chat_id_main = os.getenv("chat_id_main")
chat_id_test = os.getenv("chat_id_test")
target_time = os.getenv("target_time")
target_time2 = os.getenv("target_time2")
url = os.getenv("url")


class Environment:
    def __init__(self):
        self.token = os.getenv("token")
        self.chat_id_main = os.getenv("chat_id_main")
        self.chat_id_test = os.getenv("chat_id_test")
        self.target_time = os.getenv("target_time")
        self.target_time2 = os.getenv("target_time2")
        self.url = os.getenv("url")

    def check_tokens(self):
        """Checks the availability of environment variables."""
        missing_vars = [var for var, value in self.__dict__.items() if not value]
        if missing_vars:
            print("Required environment variables are missing:", *missing_vars)
            return False
        else:
            return True


print(Environment().check_tokens())
