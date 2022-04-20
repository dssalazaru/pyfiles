
from src import Console, Logger, Path,Debug

class Pyfiles:
    
    def __init__(self) -> None:
        # self.logger = Logger
        self.Opcion1()
        pass
    
    
    class Opcion1():
        
        def __init__(self):
            print('[Opcion 1]')
            p = Path()
            lf = self.LongFiles(p.data['files'])
            print(lf.long)

        class LongFiles:
            
            def __init__(self, files):
                self.files = files
                self.long = self.getLong()
                
                # self.exp = [(' - ', ' -', '- ')]
                # self.cmd = Console
                pass

            def getLong(self):
                ls = []
                for f in self.files:
                    if len(f) > 70:
                        ls.append(f'{len(f)}    {f}')
                        return ls
                    
            def catchExp(self, lst, exp):
                for item in lst:
                    for e in exp:
                        pass

            def updateFiles(self, data, exp):
                for item in data: # Read every item from all list
                    ndx = subItems = oldItem = nfile = ''
                    oldItem = self.path + item
                    # Split every path in list of dirs and file
                    subItems = item.split('\\\\') if '\\\\' in item else item
                    print(subItems)
                    if type(subItems) == list:
                        ndx = len(subItems) - 1
                        if ([e for e in exp] in subItems[ndx]):
                            ofile = subItems[ndx]
                            nfile = expFilter(ofile)
                        else: end = True; pass
                        nfile = nfile if ndx == 0 else '\\' + nfile
                        subItems.pop()
                    elif type(subItems) == str: continue
                    newItem = self.path + '\\'.join(subItems) + nfile
                    print('Hey')
                    # o, e = execute([con, 'mv', '"'+oldItem+'"', '"'+newItem+'"'], stdout=PIPE, stderr=PIPE).communicate()
                    # if not e:
                    #     print(f' [Done] {ofile} -> {nfile}')
                    # else: Logger.log('[Updating files]', oldItem + ' : ' + ofile + ' -> ' + nfile)
                
                def expFilter(self, item):
                    nfile = item.replace(' - ','-')
                    nfile = nfile.replace(' -','-')
                    nfile = nfile.replace('- ','-')
                    return nfile
        
    class Opcion2():
        
        def __init__(self):
            print(" Ingrese la Ruta #1")
            p1 = Path()
            print(" Ingrese la Ruta #2")
            p2 = Path()
            dir1 = p1.sortData(p1.data['d'])
            dir2 = p2.sortData(p2.data['d'])
            diff = self.compare(dir1, dir2)
            Logger.saveFile("dir1", diff[0], p1.path)
            Logger.saveFile("dir2", diff[1], p2.path)
        
        def compare(l1, l2):
            lst1 = []; lst2 = []
            [lst1.append("Not in [Ruta#1]\t" + i2) for i2 in l2 if i2 not in l1]
            [lst2.append("Not in [Ruta#2]\t" + i1) for i1 in l1 if i1 not in l2]
            return [lst1, lst2]
            
    class Opcion3():
        
        def __init__(self):
            print(" Ingrese la Ruta #1")
            p1 = Path()
            print(" Ingrese la Ruta #2")
            p2 = Path()
            all1 = p1.sortData(p1.data['all'])
            all2 = p2.sortData(p2.data['all'])
            diff = self.compare(dir1, dir2)
            Logger.saveFile("files1", diff[0], p1.path)
            Logger.saveFile("files2", diff[1], p2.path)
        
    class Opcion4():
        
        def __init__(self):
            p = Path()
            f, d = len(p.data['f']), len(p.data['d'])
            info = f"""
            > Path\t\t{p.path}
            > Total Size\t\t{p.data['s'][0]}MB\t|  {p.data['s'][1]}GB
            > Files/Dirs\t\t{f}/{d}\t|  All: {(f + d)}
            """
            print(info)

    class Opcion5():
        
        def __init__(self):
            p = Path()
            files = p.sortData(p.data['all'])
            for item in files:
                if (' - ' in item or ' -' in item or '- ' in item):
                    old = item
                    item = item.replace(' - ','-')
                    item = item.replace(' -','-')
                    item = item.replace('- ','-')
                    item = item.replace('\\','\\')
                    item = item.split('\\')
                    # cmd = f'rename "{p.path}{old}" "{item[0]}"'
                    # print(cmd)
                    # os.system(cmd)
            print(' > Finish')

        
        
