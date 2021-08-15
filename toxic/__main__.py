import logging

from aiogram import executor, Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import toxic.modules
from toxic.core import handlers

logging.basicConfig(level=logging.INFO)


import toxic.config as config

bot = Bot(
    token=config.TELEGRAM_BOT_API_TOKEN,
    parse_mode=types.ParseMode.HTML,
)
storage = MemoryStorage()
dp = Dispatcher(
    bot=bot,
    storage=storage
)

handlers.register_handlers(dp, toxic.modules.handlers)

if __name__ == '__main__':
    executor.start_polling(dp)
