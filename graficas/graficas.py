import matplotlib.pyplot as plt
import numpy as math
archivo = "./datos.csv"
# Datos
#x = np.linspace(0, 10, 100)
#y = np.sin(x)
x = ["celulares", "tablets", "portatiles", "torres", "perfericos"]
y = [10, 12, 25, 30, 45]
# Crear la gráfica
plt.bar(x,y)
plt.plot(x,y)
plt.scatter(x,y)
# Agregar título y etiquetas
plt.title('Gráfica')
plt.xlabel('productos')
plt.ylabel("ventas")

# Mostrar la gráfica
plt.show()