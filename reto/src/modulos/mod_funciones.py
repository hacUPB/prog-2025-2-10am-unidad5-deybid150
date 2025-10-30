import os
import csv
import statistics
import matplotlib.pyplot as plt

def ls():
    R = input("Ingresa la ruta (presiona Enter si ya te encuentras en la ruta deseada): ").strip()
    if R == "":
        ruta = os.getcwd()
    elif os.path.exists(R) and os.path.isdir(R):
        ruta = R
    else:
        print("La ruta o carpeta no existe. Inténtalo de nuevo.")
        return
    archivos = os.listdir(ruta)
    archivos_validos = []
    for a in archivos:
        RC = os.path.join(ruta, a)
        if os.path.isfile(RC):
            archivos_validos.append(a)

    if not archivos_validos:
        print("No se encontraron archivos en la ruta indicada.")
    else:
        for idx, nombre in enumerate(archivos_validos, start=1):
            print(f"{idx}. {nombre}")

def contar():
    R = input("Ingresa la ruta del archivo .txt: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return
    with open(R, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    palabras = contenido.split()  # IA: conteo simple de palabras
    num_palabras = len(palabras)
    num_caracteres_con_espacios = len(contenido)
    num_caracteres_sin_espacios = len(contenido.replace(" ", "").replace("\n", ""))
    print(f"Número de palabras: {num_palabras}, Número de caracteres (con espacios): {num_caracteres_con_espacios}, Número de caracteres (sin espacios): {num_caracteres_sin_espacios}")

def reemplazar():
    R = input("Ingresa la ruta del archivo .txt: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return
    PB = input("Ingresa la palabra que deseas reemplazar: ").strip()
    PN = input("Ingresa la nueva palabra: ").strip()
    with open(R, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    nuevo_contenido = contenido.replace(PB, PN)  # sencillo; si quieres límites de palabra usar regex
    with open(R, "w", encoding="utf-8") as archivo:
        archivo.write(nuevo_contenido)
    print("Se reemplazó", PB, "por", PN)

def histograma():
    R = input("Ingresa la ruta del archivo .txt: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return

    with open(R, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().lower()

    a = e = ii = o = u = 0  #IA ii para no chocar con índice i si se usa en otro contexto
    pos = 0

    while pos < len(contenido):
        c = contenido[pos]
        if c == "a":
            a += 1
        elif c == "e":
            e += 1
        elif c == "i":
            ii += 1
        elif c == "o":
            o += 1
        elif c == "u":
            u += 1
        pos += 1

    vocales = ["a", "e", "i", "o", "u"]
    valores = [a, e, ii, o, u]

    plt.bar(vocales, valores)
    plt.title("Histograma de ocurrencia de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Cantidad")
    plt.show()

    print("Conteo de vocales:", "a =", a, "e =", e, "i =", ii, "o =", o, "u =", u)

def M15():
    R = input("Ingresa la ruta del archivo .csv: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return
    with open(R, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = [f for f in lector]
    print("Mostrando las primeras 15 filas del archivo:\n")
    for f in filas[:15]:
        print(f)

def Calcular_Estadísticas():
    R = input("Ingresa la ruta del archivo .csv: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return
    with open(R, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = [f for f in lector]
    if not filas:
        print("El archivo está vacío.")
        return
    indice = input("Ingresa el número de la columna: ").strip()
    if not indice.isdigit():
        print("Índice no válido.")
        return
    indice = int(indice)
    valores = []
    for fila in filas[1:]:
        if indice < len(fila):
            celda = fila[indice].strip()
            if celda != "":
                try:
                    valores.append(float(celda))
                except ValueError:
                    continue
    if valores:
        cantidad = len(valores)
        promedio = statistics.mean(valores)
        mediana = statistics.median(valores)
        desviacion = statistics.stdev(valores) if cantidad > 1 else 0
        print(f"\nResultados estadísticos:\nNumero de datos: {cantidad}\nPromedio: {promedio}\nMediana: {mediana}\nDesviación estándar: {desviacion}\nValor máximo: {max(valores)}\nValor mínimo: {min(valores)}")
    else:
        print("No se encontraron datos numéricos ;(")

def graficar():
    R = input("Ingresa la ruta del archivo .csv: ").strip()
    if not os.path.exists(R) or not os.path.isfile(R):
        print("El archivo no existe.")
        return
    with open(R, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        filas = [f for f in lector]
    if not filas:
        print("Archivo vacío.")
        return
    cabeza = filas[0]
    for i, col in enumerate(cabeza):
        print(f"{i}. {col}")
    indice = input("Ingresa el número de la columna que deseas graficar: ").strip()
    if not indice.isdigit():
        print("Índice no válido.")
        return
    indice = int(indice)
    valores = []
    for fila in filas[1:]:
        if indice < len(fila):
            celda = fila[indice].strip()
            try:
                valores.append(float(celda))
            except ValueError:
                continue
    if not valores:
        print("No hay datos numéricos para graficar.")
        return
    x = list(range(len(valores)))
    y = valores
    plt.scatter(x, y)
    plt.title("Gráfico de dispersión")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.show()
    copia = sorted(valores)  # IA: usar sorted en lugar de burbuja
    etiquetas = [str(i) for i in range(len(copia))]
    plt.bar(etiquetas, copia)
    plt.title("Gráfico de barras (valores ordenados)")
    plt.xlabel("Índice ordenado")
    plt.ylabel("Valor")
    plt.show()


