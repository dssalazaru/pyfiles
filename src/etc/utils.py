from os import get_terminal_size
from pathlib import Path as p

from src.console import Console

class Utils:

    mainpath = p(__file__).resolve().parent.parent.parent

    def stopPyfiles():
        exit()

    class Banner:
        def __init__(self, action):
            self.data = {'name':'Python File Manager', 'by':"@dssalazaru", 'ver':"v3.0"}
            self.size = get_terminal_size().columns
            self.br = f"\n{'-' * self.size}\n"
            if action == "print": Console.clear(); print(self.banner())
            elif action == "br": print(self.separator())

        def banner(self):
            return f"{self.br}{' '.join(self.data.values()).center(self.size,' ')}{self.br}"
        
        def separator(self):
            return self.br