from toxic.core.handlers import Handler
from .handlers import run_rust_code

handlers_list = [
    Handler(
        type='message',
        callback=run_rust_code,
        args={
            'commands': ['rust']
        }
    )
]
