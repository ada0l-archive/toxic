import aiohttp
import json

from toxic.loader import dp
from aiogram import types


@dp.message_handler(commands=['rust'])
async def run_rust_code(message: types.Message):
    program_text = message.text[message.text.index(' '):]
    data = {
        'code': str(program_text),
        'version': "stable",
        'optimize': '0',
        'test': False,
        'color': True,
        'backtrace': '0'
    }

    url_to_playground = "https://play.rust-lang.org/evaluate.json"

    async with aiohttp.ClientSession() as session:
        response = await session.post(url_to_playground, data=json.dumps(data))
        async with response:
            if response.status != 200:
                await message.reply(f'Status code {response.status}')
            else:
                result = await response.text()
                result_json = json.loads(result)
                await message.reply(f"Error: {result_json['error']}\n"
                                    "Output:\n"
                                    f"{result_json['result']}")
