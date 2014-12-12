import asyncio
import re


class Carrier:
    match_regex = r'/(?=a)b/'  # Always false regex to prevent matching against base class

    def __init__(self):
        pass

    @asyncio.coroutine
    def startup(self):
        pass

    @asyncio.coroutine
    def track(self, id):
        pass

    def match_package(self, id):
        return re.match(self.match_regex, id)

