def 

def sub_txt():
    e = True
    while e == True:
        print("C. Contar número de palabras y caracteres\nR. Reemplazar una palabra por otra\nH. Histograma de ocurrencia de las vocales\nS. Salir")
        T = input("elige que quieres hacer con tu archivo de texto: ").upper
        match T:
            case "C":

            case "R":

            case "H":

            case "S":
                print("saliendo...")
                e = False
            case _:
                print("modo no valido")
                break  

def sub_csv():
    e = True
    while e == True:
        print("M. Mostrar las 15 primeras filas\nC. Calcular Estadísticas\nG. Graficar una columna completa con los datos\nS. Salir")
        T = input("elige que quieres hacer con tu archivo .CSV: ").upper
        match T:
            case "M":

            case "C":

            case "G":

            case "S":
                print("saliendo...")
                e = False
            case _:
                print("modo no valido")
                break  