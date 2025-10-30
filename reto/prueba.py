import csv
import os
import statistics
ruta = input("Ingresa la ruta del archivo .csv: ").strip()
if not os.path.exists(ruta):
    print("El archivo no existe.")
else:
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = []
        for fila in lector:
            filas.append(fila)

    encabezado = filas[0]
    print("Columnas disponibles:")
    i = 0
    while i < len(encabezado):
        print(f"{i}. {encabezado[i]}")
        i += 1

    indice = input("Ingresa el número de la columna que deseas analizar: ").strip()
    if indice.isdigit():
        indice = int(indice)
        valores = []
        i = 1
        while i < len(filas):
            if indice < len(filas[i]):
                celda = filas[i][indice].strip()
                if celda != "":
                    if celda.replace(".", "", 1).isdigit():
                        valores.append(float(celda))
            i += 1

        if len(valores) > 0:
            cantidad = len(valores)
            promedio = statistics.mean(valores)
            mediana = statistics.median(valores)
            if cantidad > 1:
                desviacion = statistics.stdev(valores)
            else:
                desviacion = 0
            maximo = max(valores)
            minimo = min(valores)
            print(f"\nResultados estadísticos: \nNumero de datos: {cantidad}\nPromedio: {promedio}\nMediana: {mediana}\nDesviación estándar: {desviacion}\nValor máximo: {maximo}\nValor mínimo: {minimo}")
        else:
            print("No hay datos numéricos en esta columna.")
    else:
        print("Entrada no válida.")