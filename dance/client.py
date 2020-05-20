from .api import HttpClient
import asks
import socketio as socket
import time

class Client():
    """
    Represents a client that connects to nertivia

    This class is the core of the library with all of its functionality revolving around it.
    """
    def __init__(self, **kwargs):
        self.token = ''
        self.is_bot = True
        self.load_time = None
        self.api = HttpClient(self)
        self.session = asks.Session()

    def close(self):
        if self.is_bot:
            self.close()

    def connect(self, token):
        self.load_time = time.time()
        self.token = self.api.token = token
        socket.Client().emit('authentication', { 'token': token })
        socket.Client().connect('https://nertivia.supertiger.tk')
        
