import json

import aiohttp
from aiogram.utils.exceptions import CantParseEntities


class Playground:
    url = "https://play.rust-lang.org/evaluate.json"

    @staticmethod
    async def execute(code: str) -> (str, str):
        data = {
            'code': code,
            'version': "stable",
            'optimize': '0',
            'test': False,
            'color': True,
            'backtrace': '0'
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(Playground.url, data=json.dumps(data))
            async with response:
                if response.status != 200:
                    return (
                        'Bad request to rust playground',
                        '',
                    )
                else:
                    result = await response.text()
                    result_json = json.loads(result)
                    try:
                        return (
                            result_json['error'],
                            result_json['result'],
                        )
                    except CantParseEntities:
                        return (
                            'Bad processing',
                            '',
                        )


class PlaygroundResultConverter:

    @staticmethod
    def to_string(error: str, output: str):
        if output == '':
            return f'Error: {error}'
        if error is None:
            return f'◾OK!\n' \
                   f'◾Output:\n{output}'
        else:
            return f'◾{error}'
