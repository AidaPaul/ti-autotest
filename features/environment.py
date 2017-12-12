from settings import host, user
from telnetlib import Telnet
import time


def search_buffer(buffer, phrase):
    if buffer.find(phrase) == -1:
        return False
    else:
        return True


class MudClient(Telnet):
    buffer = ''

    def command_and_store(self, command, sleep=2):
        raw = ("%s\n" % command).encode()
        self.write(raw)
        time.sleep(sleep)
        result = self.read_very_eager().decode()
        self.buffer += result
        return result

    def get_and_clear_buffer(self):
        buffer = self.buffer
        self.buffer = ''
        return buffer

    def login(self, name, password):
        self.command_and_store(name)
        self.command_and_store(password)
        self.command_and_store('')

    def set_prompt(self):
        self.command_and_store('prompt Room name: %r')

    def __del__(self):
        self.command_and_store('quit')
        super(MudClient, self).__del__()
        return self.get_and_clear_buffer()
        

def before_scenario(context, scenario):
    context.search_buffer = search_buffer
    context.config.setup_logging()
    context.connection = MudClient(**host)
    context.connection.login(**user)
    context.buffers = {
        'login': context.connection.get_and_clear_buffer()
    }
    context.connection.set_prompt()
