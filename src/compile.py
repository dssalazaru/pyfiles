from os import system

from .etc import Utils

class Compile():
    
    def __init__(self,code):
        self.code = code
        compile()

    def runCompile(self):
        if (self.code == "DSCode"): 
            system(f'pyinstaller --onefile {Utils.mainpath} --name pyfiles'); exit()