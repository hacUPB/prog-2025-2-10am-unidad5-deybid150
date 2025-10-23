import csv
with open("./Archivos/TABLA.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    print(encabezado[0])
    presion = []
    for fila in lector:
        p = float(fila[0])
        presion.append(p)
    print(sum(presion), "mmhg")
    
    csvfile.seek(0)
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    print(encabezado[1])
    temperatura = []
    for fila in lector:
        t = float(fila[1])
        temperatura.append(t)
    print(sum(temperatura), "°C")
    
    csvfile.seek(0)
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    print(encabezado[2])
    humedad = []
    for fila in lector:
        h = int(fila[2])
        humedad.append(h)
    print(sum(humedad), "%")
    
    csvfile.seek(0)
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    print(encabezado[3])
    densidad = []
    for fila in lector:
        fila[3] = fila[3].replace(",",".")
        d = float(fila[3])
        densidad.append(d)
    print(sum(densidad), "kg/m^3")
    

        