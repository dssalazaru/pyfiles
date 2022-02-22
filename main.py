# -------------------------------------------------------- #
# |   Python File Manager  |  Python Script by dssu.me   | #
# -------------------------------------------------------- #

# imports 
import os, datetime

# ------------------------------------------------------------- #
date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")    #
name, by, ver = "Python File Manager", "@dssalazaru", "v3.0"    #
br = f"\n{'-'*(len(name) + len(by) + len(ver) + 17)}\n"         #
# ------------------------------------------------------------- #

# Main function
def main():
    # Stating date and log file
    log(f'[Running {ver}]', ('--> '*15) + '\n')
    # Start program loop
    menu()
    # End of the program
    input("\n # Done, pulse cualquier tecla para salir...")

def banner():
    return f"{br}\t{name} {by} {ver}{br}"
    
def menu():
    opt = 0
    options = """     1) Examinar rutas mayores a 240 caracteres.
     2) Encontrar Carpetas diferentes entre 2 rutas.
     3) Encontrar TODAS las diferentes entre 2 rutas.
     4) Evaluar tamaño & conteo de Archivos y Carpetas. 
    """
    while(True):
        print(banner() + options)
        try:
            opt = int(input(" * Proceso a ejecutar > ").strip())
        except Exception: pass
        if (opt != "" and opt > 0 and opt < 5): break
        else: os.system("cls")
    print(br)
    if opt == 1: opcion1()
    elif opt == 2: opcion2()
    elif opt == 3: opcion3()
    elif opt == 4: opcion4()
        
def opcion1():
    p = Path()
    lf = longFiles(p.data['f'])
    saveFile("long", lf, p.path)

def opcion2():
    print(" Ingrese la Ruta #1")
    p1 = Path()
    print(" Ingrese la Ruta #2")
    p2 = Path()
    dir1 = p1.sortData(p1.data['d'])
    dir2 = p2.sortData(p2.data['d'])
    diff = compare(dir1, dir2)
    saveFile("dir1", diff[0], p1.path)
    saveFile("dir2", diff[1], p2.path)
    
def opcion3():
    print(" Ingrese la Ruta #1")
    p1 = Path()
    print(" Ingrese la Ruta #2")
    p2 = Path()
    all1 = p1.sortData(p1.data['all'])
    all2 = p2.sortData(p2.data['all'])
    diff = compare(all1, all2)
    saveFile("files1", diff[0], p1.path)
    saveFile("files2", diff[1], p2.path)
    
def opcion4():
    p = Path()
    f, d = len(p.data['f']), len(p.data['d'])
    info = f"""
  > Path\t\t{p.path}
  > Total Size\t\t{p.data['s'][0]}MB\t|  {p.data['s'][1]}GB
  > Files/Dirs\t\t{f}/{d}\t|  All: {(f + d)}
    """
    print(info)

def longFiles(lst):
    lf = []
    [lf.append(f"{len(f)}\t{f}") for f in lst if len(f) >= 230]
    return lf

def compare(l1, l2):
    lst1 = []; lst2 = []
    [lst1.append("Not in [Ruta#1]\t" + i2) for i2 in l2 if i2 not in l1]
    [lst2.append("Not in [Ruta#2]\t" + i1) for i1 in l1 if i1 not in l2]
    return [lst1, lst2]

def log(func, e):
    file = 'pyfiles_events.log'
    if os.path.isfile(file): mode = 'a'
    else: mode = 'w'
    with open(file, mode, encoding="utf-8") as f:
        f.write(f'[{date}]{func} --> {e}\n')
        f.close
    print(' ! Error in {}, more info in [{}]'.format(func,file))    
        
def saveFile(process, lst, path):
    try:
        with open(f"pyfiles_{process}.txt", "w", encoding="utf-8") as f:
            f.write(f'[{date}] {path}\n')
            [f.writelines(f"{line}\n") for line in lst]
    except Exception as e: log("[saveFile]",e)

def compile(code):
    if (code == "DSCode"): os.system(f'pyinstaller --onefile {os.path.realpath(__file__)} --name pyfiles && pause && exit')

class Path():

    def __init__(self):
        self.getPath()
        self.readPath()
        try:
            tmp = list(map(self.checkDup, [lst for lst in list(self.data.values())]))
            self.data = {'all': tmp[0], 'f': tmp[1], 'd': tmp[2], 's': tmp[3]}
        except Exception as e: log('[Class: Path] data not fetch', e)
            
    def getPath(self):
        try:
            while(True):
                path = input(" * Ruta: ").strip()
                if(path == "."): self.path = os.path.dirname(os.path.realpath(__file__)); break
                elif(path != ""): self.path = path; break
            print(br)
        except Exception as e: log("[getPath]",e)
        
    def readPath(self):
        al = []; fl = []; dl = []; sz = 0
        for root, directories, files in os.walk(self.path, topdown=False):
            for name in files:
                try:
                    f = os.path.join(root, name)
                    fsz = os.path.getsize(f)
                    fl.append(f) 
                    al.append(str(round((fsz/(1024**2)),2))+"MB\t"+f)
                    sz += fsz
                except Exception as e: log("[readPath : files]",e)
            for name in directories:
                try:
                    d = os.path.join(root, name)
                    al.append(d)
                    dl.append(d)
                except Exception as e: log("[readPath : dirs]",e)
        sz = [(round(sz/(1024**2),2)), (round(sz/(1024**3),2))]
        self.data = {'all': al, 'f': fl, 'd': dl, 's': sz}

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
        except Exception as e: log("[checkDup]",e)
    
# Run program
if __name__ == "__main__":
    main()
    