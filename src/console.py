from platform import system
from subprocess import Popen as execute
from subprocess import PIPE

class Console:

    def __init__(self):
        self.con = 'powershell' if system().lower() == 'windows' else self.command('exit')

    def command(self, *args, **kwargs):
        if kwargs['cmd'] == 'lspath': self.cmd = [self.con, 'ls', '-Path', kwargs['p'], '-n', '-r']
        elif kwargs['cmd'] == 'rename': self.cmd = self.cmd = [self.con, 'mv', '"'+kwargs['f1']+'"', '"'+kwargs['f2']+'"']
        else:
            for arg in args:
                self.cmd = [self.con,]
        self.runCommand()
        
    def clear():
        execute(['powershell','cls']).wait()

    def runCommand(self):
        o,e = execute(self.cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
        if not e: self.result = o
        else: self.error = f'[Console] Error in command: {self.cmd[0]}'
    