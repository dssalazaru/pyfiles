# ---------------------------------------------------------
#   Banner and program info - Python Script by dssudev.co
# ---------------------------------------------------------

# imports 
import os

# Main function
def main():
    # Start program loop
    menu()
    # End of the program
    input("\n # Done, pulse cualquier tecla para salir...")

def banner():
    global br
    name, by, ver = "Python File Manager", "@dssalazaru", "v3.0"
    br = f"\n{'-'*(len(name) + len(by) + len(ver) + 17)}\n"
    title = f"{br}\t{name} {by} {ver}{br}"
    print(title)
    
def menu():
    opt = 0
    opcions = """     1) Examinar rutas mayores a 240 caracteres.
     2) Encontrar Carpetas diferentes entre 2 rutas.
     3) Encontrar TODAS las diferentes entre 2 rutas.
     4) Evaluar tamaño & conteo de Archivos y Carpetas. 
    """
    while(True):
        banner()
        print(opcions)
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
    saveFile("long", lf) # Check duplicates and Save final Log

def opcion2():
    print(" Ingrese la Ruta #1")
    p1 = Path()
    print(" Ingrese la Ruta #2")
    p2 = Path()
    dir1 = p1.sortData(p1.data['d'])
    dir2 = p2.sortData(p2.data['d'])
    diff = compare(dir1, dir2)
    saveFile("dir1", diff[0])
    saveFile("dir2", diff[1])
    
def opcion3():
    print(" Ingrese la Ruta #1")
    p1 = Path()
    print(" Ingrese la Ruta #2")
    p2 = Path()
    all1 = p1.sortData(p1.data['all'])
    all2 = p2.sortData(p2.data['all'])
    diff = compare(all1, all2)
    saveFile("files1", diff[0])
    saveFile("files2", diff[1])
    
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

def error(func, e):
    if os.path.isfile('error.log'): mode = 'a'
    else: mode = 'w'
    with open(f"pyfiles_error.log", mode, encoding="utf-8") as f:
        f.write(f' {func} --> {e}\n')
        f.close
    input("")
        
def saveFile(process, lst):
    try:
        with open(f"pyfiles_{process}.txt", "w", encoding="utf-8") as f: # Create the final file
            [f.writelines(f"{line}\n") for line in lst] # Save all lines
    except Exception as e: error("[saveFile]",e)

def compile(code):
    if (code == "DSCode"): os.system('pyinstaller --onefile main.py --name program && pause && exit') # Compile

class Path():

    def __init__(self):
        self.getPath()
        self.readPath()
        try:
            tmp = list(map(self.checkDup, [lst for lst in list(self.data.values())]))
            self.data = {'all': tmp[0], 'f': tmp[1], 'd': tmp[2], 's': tmp[3]}
        except Exception as e: error('[Class: Path] data not fetch', e)
            
    def getPath(self):
        try:
            while(True): # While the path is blank repeat
                path = input(" * Ruta: ").strip()
                if(path == "."): self.path = os.path.dirname(os.path.realpath(__file__)); break
                elif(path != ""): self.path = path; break
            print(br)
        except Exception as e: error("[getPath]",e)
        
    def readPath(self):
        al = []; fl = []; dl = []; sz = 0
        try:
            for root, directories, files in os.walk(self.path, topdown=False): # Walk for all files 
                for name in files:
                    f = os.path.join(root, name)
                    fsz = os.path.getsize(f)
                    fl.append(f) 
                    al.append(str(round((fsz/(1024**2)),2))+"MB\t"+f) # Append all files in general lst
                    sz += fsz
                for name in directories:
                    d = os.path.join(root, name)
                    al.append(d)
                    dl.append(d)
            sz = [(round(sz/(1024**2),2)), (round(sz/(1024**3),2))]
            self.data = {'all': al, 'f': fl, 'd': dl, 's': sz}
        except Exception as e: error("[readPath]",e)

    def sortData(self, lst):
        lst.sort()
        return [i.replace(self.path, '') for i in lst]
    
    def checkDup(self, lst):
        try:
            if (type(lst) != 'list'): return lst
            for line in lst: # Read al lines in lst for chech
                if lst.count(line) > 1: # if are more that one time
                    print(" * Duplicado: ",line) # Print in console
                    lst.remove(line) # Remove duplicate entry
            return lst # Return the new lst
        except Exception as e: error("[checkDup]",e)
    
# Run program
if __name__ == "__main__":
    main()
    