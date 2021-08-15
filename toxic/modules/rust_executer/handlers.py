from aiogram import types

from .playground import Playground, PlaygroundResultConverter


async def run_rust_code(message: types.Message):
    try:
        program_text = message.text[message.text.index(' '):]
    except ValueError:
        await message.reply('The program text is empty')
        return
    else:
        await message.reply('I am trying to compile...')

    result = await Playground.execute(program_text)
    await message.reply(PlaygroundResultConverter.to_string(*result))
