archivo = open("./Archivos/ej1.txt","r")
for i in range(2):
    archivo.readline()
archivo.seek(12)
datos = archivo.readline()
print(datos)
archivo.close()
'''    
archivo.read(11)
datos = archivo.readline()
print(datos)
archivo.close()
'''