ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
# "\" se usa para comandos de texto
nombre_archivo = "frutas.txt"
modo = "x" #"w" solo escritura - sobreescribe, "x" verifica que sea unico, "r" solo lectura, 
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding = "UTF-8")

# solicitar una variable entera y una float al usuario y escribirla en el archivo
edad= int(input("ingrese su edad: "))
estatura = float(input("¿cuanto mides? "))
frase = input("ingrese su nombre y que estudia: ")
fp.write(str(estatura) + "\n")
fp.write(str(edad)+ "\n")
fp.write(frase + "\n")

fp.close()
