from datetime import datetime as dt

class Time:
    dati = dt.now().strftime("%d-%m-%Y %H:%M:%S")
    date = dt.now().strftime("%d-%m-%Y")
    time = dt.now().strftime("%H:%M:%S")