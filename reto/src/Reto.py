from mod_funciones import *

i = True
while i == True:
    print("1. Contar número de palabras y caracteres\n2. Procesar archivo de texto (.txt)\n3. Procesar archivo separado por comas (.csv)\n4. Salir")
    T = int(input("elige que quieres hacer con tu archivo de texto: "))
    match T:
        case 1:
            pass 
        case 2:
            sub_text()
        case 3:
            sub_csv()
        case 4:
            print("saliendo...")
            i = False
        case _:
            print("modo no valido")
            break