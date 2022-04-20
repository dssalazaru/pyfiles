from os import path

from .etc import Time,Utils

class Logger:

    def __init__(self, *args, **kwargs):
        self.path = str(Utils.mainpath) + '\\logs\\'
        self.origin = __name__
        self.func = args[0]
        self.dt = Time
        self.er = kwargs['er']
        self.type = 'error' if kwargs['er'] else 'event'
        self.log()

    def log(self):
        file = self.path + f'pyfiles_{self.type}.log'
        mode = 'a' if path.isfile(file) else 'w'
        with open(file, mode, encoding="utf-8") as f:
            line = f'[{self.dt.dati}][{self.origin}][{self.func}] --> {self.er}\n'
            f.write(line)
            print(line)
        # print(f' ! [Debug][{self.date}]{func}, more info in [{file}]')

    # def error(**kwargs):
    #     file = 'pyfiles_error.log'
    #     if path.isfile(file): mode = 'a'
    #     else: mode = 'w'
    #     with open(file, mode, encoding="utf-8") as f:
    #         f.write(f'[{Time.dati}]{kwargs["func"]} --> {kwargs["error"]}\n')
    #         f.close
    #     print(f' ! [Error][{Time.dati}]{kwargs["func"]}, more info in [{file}]')

    def saveFile(self, process, lst, path):
        try:
            with open(f"{self.path}\\pyfiles_{process}.txt", "w", encoding="utf-8") as f:
                f.write(f'[{self.date}] {path}\n')
                [f.writelines(f"{line}\n") for line in lst]
        except Exception as e: self.log("[saveFile]",e)