import asyncio
import tornado
from tornado.platform.asyncio import AsyncIOMainLoop

class App:
    def __init__(self):
        self.setup_networking()

    def setup_networking(self):
        self.loop = asyncio.get_event_loop()
        AsyncIOMainLoop().install()

    def run(self):
        pass


def setup_networking():
    loop = asyncio.get_event_loop()


if __name__ == "__main__":

    asyncio.get_event_loop().run_forever()