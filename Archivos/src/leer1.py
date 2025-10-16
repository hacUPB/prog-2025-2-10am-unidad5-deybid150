
archivo = open("./archivos/texto.txt","r")
#for  i in range(5):  
#    datos = archivo.readline() /archivo.read() #EOF = final de archivo(End Of File)
#for datos in archivo:
#    print(datos[0])
datos = archivo.readlines() #denota cada linea como un elemento de una lista
print(datos)
archivo.close()
