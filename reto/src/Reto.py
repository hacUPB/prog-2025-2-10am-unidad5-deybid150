#IA usar import absoluto si ejecutas este archivo como script
from modulos.mod_funciones import *

i = True
while i == True:
    print("1. Contar número de palabras y caracteres\n2. Procesar archivo de texto (.txt)\n3. Procesar archivo separado por comas (.csv)\n4. Salir")
    T = int(input("elige que quieres hacer: "))
    match T:
        case 1:
            ls() 
        case 2:
            e = True
            while e == True:
                print("C. Contar número de palabras y caracteres\nR. Reemplazar una palabra por otra\nH. Histograma de ocurrencia de las vocales\nS. Salir")
                T = input("elige que quieres hacer con tu archivo de texto: ").strip().upper()  #IA <-- fix: llamar .upper()
                match T:
                    case "C":
                        contar()
                    case "R":
                        reemplazar()
                    case "H":
                        histograma()
                    case "S":
                        print("saliendo...")
                        e = False
                    case _:
                        print("modo no valido")
                        break
        case 3:
            e = True
            while e == True:
                print("M. Mostrar las 15 primeras filas\nC. Calcular Estadísticas\nG. Graficar una columna completa con los datos\nS. Salir")
                T = input("elige que quieres hacer con tu archivo .CSV: ").strip().upper()  #IA <-- fix: llamar .upper()
                match T:
                    case "M":
                        M15()
                    case "C":
                        Calcular_Estadísticas()
                    case "G":
                        graficar()
                    case "S":
                        print("saliendo...")
                        e = False
                    case _:
                        print("modo no valido")
                        break
        case 4:
            print("saliendo...")
            i = False
        case _:
            print("modo no valido")
            break