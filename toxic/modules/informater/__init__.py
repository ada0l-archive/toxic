from toxic.core.handlers import Handler
from .handlers import send_welcome

handlers_list = [
    Handler(
        type='message',
        callback=send_welcome,
        args={
            'commands': ['start', 'help']
        }
    )
]
