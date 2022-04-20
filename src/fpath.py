from os import path as ospath
from os import walk

from src import Logger
from .etc import Utils,Debug

class Path():
    
    def __init__(self):
        self.data = {'all': [], 'filesize': [], 'files': [], 'dirs': [], 'size': {}}
        self.mode = Debug(True)  
        if self.mode.isEnabled():
            self.path = self.mode.testpath()
        else: 
            self.path = self.getPath()
        self.getData()
        # try:
        #     tmp = list(map(self.checkDup, [lst for lst in list(self.data.values())]))
        #     self.data = {'all': tmp[0], 'f': tmp[1], 'd': tmp[2], 's': tmp[3]}
        # except Exception as e: Logger.error('[Class: Path] data not fetch', e)
            
    def getPath(self):
        try:
            while(True):
                path = input(" * Ruta: ").strip()
                if(path == "."): return Utils.mainpath; break
                elif(path != ""): return path; break
        except Exception as e: Logger("[getPath]",er=e)
        
    def getData(self):
        sz = 0
        for root, directories, files in walk(self.path, topdown=False):
            for name in files:
                try:
                    f = ospath.join(root, name)
                    fsz = ospath.getsize(f)
                    self.data['files'].append(f) 
                    self.data['filesize'].append(str(round((fsz/(1024**2)),2))+"MB    "+f)
                    sz += fsz
                except Exception as e: print("e"); Logger("[getData : files]",er=e)
            for name in directories:
                try:
                    d = ospath.join(root, name)
                    self.data['dirs'].append(d)
                except Exception as e: Logger("[getData : dirs]",er=e)
        self.data['all'] = self.data['files'] + self.data['dirs']
        self.data['size'] = {'mb':(round(sz/(1024**2),2)), 'gb':(round(sz/(1024**3),2))}


    def sortData(self, lst):
        lst.sort()
        return [i.replace(self.path, '') for i in lst]
    
    def checkDup(self, lst):
        try:
            if (type(lst) != 'list'): return lst
            for line in lst: 
                if lst.count(line) > 1:
                    print(" * Duplicado: ",line)
                    lst.remove(line)
            return lst 
        except Exception as e: Logger("[checkDup]",er=e)