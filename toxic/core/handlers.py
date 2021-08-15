from collections import namedtuple

Handler = namedtuple('Handle', ['type', 'callback', 'args'])


def register_handler(dp, handler: Handler):
    if handler.type == 'message':
        dp.register_message_handler(
            handler.callback,
            **handler.args
        )


def register_handlers(dp, handlers: [Handler]):
    for handler in handlers:
        register_handler(dp, handler)
