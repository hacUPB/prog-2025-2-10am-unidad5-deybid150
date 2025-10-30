nombre_archivo = "./Archivos/texto.txt"
with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
    lista = archivo.readlines()
    for c in lista:
        print(c)