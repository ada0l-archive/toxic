from toxic.loader import dp
from aiogram import types


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi\n"
                        "I'm toxic bot")
