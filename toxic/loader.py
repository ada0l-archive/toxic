from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import toxic.config as config

bot = Bot(
    token=config.TELEGRAM_BOT_API_TOKEN,
    parse_mode=types.ParseMode.HTML
)
storage = MemoryStorage()
dp = Dispatcher(
    bot=bot,
    storage=storage
)
