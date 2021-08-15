from aiogram import executor
from toxic.loader import dp
import toxic.handlers
import logging


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp)
