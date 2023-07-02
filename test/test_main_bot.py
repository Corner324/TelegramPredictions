from unittest.mock import MagicMock
import unittest
from aiogram import Bot, types
import asyncio

# Импорт вашего модуля с ботом
import main_bot
import logger
import config

class TestBot(unittest.TestCase):
    async def test_start_handler(self):
        # Создаем моки для объектов, необходимых для функции
        bot = MagicMock(spec=Bot)
        message = MagicMock(spec=types.Message)
        message.reply = MagicMock()
        logger.send_logs = MagicMock()

        # Устанавливаем значения для минуты и часа
        minu = '30'
        hour = '10'

        # Мокируем функции, которые используются внутри функции start_handler
        main_bot.get_optimize_min = MagicMock(return_value=minu)
        main_bot.get_hours = MagicMock(return_value=hour)
        config.target_time = '11:00'

        # Вызываем функцию для тестирования
        await main_bot.start_handler(message)

        # Проверяем ожидаемое поведение
        expected_response = f'Current time - {hour}:{minu}\nTarget time - {config.target_time}\n'
        message.reply.assert_called_once_with(expected_response)
        # logger.send_logs.assert_called_once_with(bot, message)

if __name__ == '__main__':
    # Запуск тестов
    test_Bot = TestBot()
    asyncio.run(test_Bot.test_start_handler())
