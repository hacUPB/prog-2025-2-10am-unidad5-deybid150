nombre_archivo = input("ingrese el nombre del archivo a crear: ")
with open(nombre_archivo, "w", encoding="UTF-8") as fp:
    edad= int(input("ingrese su edad: "))
    estatura = float(input("¿cuanto mides? "))
    frase = input("ingrese su nombre y que estudia: ")
    fp.write(str(estatura) + "\n")
    fp.write(str(edad)+ "\n")
    fp.write(frase + "\n")
