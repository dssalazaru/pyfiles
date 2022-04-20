# -------------------------------------------------------- #
# |   Python File Manager  |  Python Script by dssu.me   | #
# -------------------------------------------------------- #

# imports

from src import Path, Debug, Utils, Pyfiles


        # try:
        #     if not e:
        #         # files = str(o).replace("b'",'').replace("'",'').replace('\\\\', '\\').split('\\r\\n')
        #         files = [item for item in reversed(files) if item]
        #         # print(files)
        #         # print(list(map(lambda files,exp: exp in files, files,exp1)))
        # except Exception as e: Logger.log('[error] al listar los archivos',e)
        


# Main function
def main():
    mode = Debug(True)  
    
    if mode.isEnabled():
        Pyfiles()
    else: 
        menu()
    
    
    
    
    # Stating date and log file
    # log(f'[Running {ver}]', ('--> '*15) + '\n')
    # Start program loop
    # lsPath(path)
    # print(ls)
    # list(map(lambda l: updateFiles(l), data))
    # menu()
    # End of the program
    # input("\n # Done, pulse cualquier tecla para salir...")


def menu():
    opt = 0
    options = """     1) Examinar rutas mayores a 240 caracteres.
     2) Encontrar Carpetas diferentes entre 2 rutas.
     3) Encontrar TODAS las diferentes entre 2 rutas.
     4) Evaluar tamaño & conteo de Archivos y Carpetas.
     5) Remove giones en nombres [ - ] => [-] 
    """
    while(True):
        Utils.Banner('print')
        print(options)
        try:
            dat = input(" * Proceso a ejecutar > ").strip()
            opt = int(dat)
        except Exception: None
        if (opt != "" and opt > 0 and opt < 6): break
        else: print('\n\n')
    Utils.Banner('br')
    if opt == 1: Pyfiles.Opcion1()
    # elif opt == 2: opcion2()
    # elif opt == 3: opcion3()
    # elif opt == 4: opcion4()
    # elif opt == 5: opcion5()
        


def longFiles(lst):
    lf = []
    [lf.append(f"{len(f)}\t{f}") for f in lst if len(f) >= 230]
    return lf


    
# Run program
if __name__ == "__main__":
    main()
    