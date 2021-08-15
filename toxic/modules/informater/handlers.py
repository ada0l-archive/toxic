from aiogram import types


async def send_welcome(message: types.Message):
    await message.reply("Hi\n"
                        "I'm toxic bot")
