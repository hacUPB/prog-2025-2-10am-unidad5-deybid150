lista = ["ride it","esta cobardia","sunset lover","quizás","cold"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivos\\"
modo = "x"
nombre_archivo = "Canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="UTF-8")
for cancion in lista:
    fp.write(cancion + "\n")
fp.close()
