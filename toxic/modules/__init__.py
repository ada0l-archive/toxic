from . import informater
from . import rust_executer

handlers = []
handlers += informater.handlers_list
handlers += rust_executer.handlers_list
