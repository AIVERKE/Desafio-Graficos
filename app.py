import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones correspondientes a cada ecuación
def eq1(x2):
    return 2 - 1.0001 * x2  # x1 = 2 - 1.0001*x2

def eq2(x2):
    return 2 - x2  # x1 = 2 - x2

# Crear un rango de valores para x2
x2_vals = np.linspace(0, 2, 100)

# Calcular los valores correspondientes de x1 para cada ecuación
x1_vals_eq1 = eq1(x2_vals)
x1_vals_eq2 = eq2(x2_vals)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x2_vals, x1_vals_eq1, label=r'$x_1 + 1.0001x_2 = 2$', color='b')
plt.plot(x2_vals, x1_vals_eq2, label=r'$x_1 + x_2 = 2$', color='g')

# Añadir etiquetas y título
plt.xlabel(r'$x_2$')
plt.ylabel(r'$x_1$')
plt.title('Gráfica de las ecuaciones del sistema mal condicionado')

# Añadir una leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()
