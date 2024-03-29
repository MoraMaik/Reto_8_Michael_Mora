import math

# Definir la función para calcular una aproximación de e**x
def aproximar_exponencial(x, n):
    suma = 0.0
    # Calcular la sumatoria de los términos de la serie de Maclaurin
    for i in range(n + 1):
        # Añadir el término actual a la suma
        suma += x ** i / math.factorial(i)
    return suma
# Solicitar ingresar el valor de x
x = float(input("Ingrese el valor de x para calcular e^x: "))
# Solicitar ingresar el número de términos n
n = int(input("Ingrese el número de términos n para la aproximación: "))
# Calcular la aproximación
aproximacion = aproximar_exponencial(x, n)
# Calcular el valor real usando math.exp
valor_real = math.exp(x)
# Mostrar la aproximación y la diferencia con el valor real
print(f"Aproximación de e^{x} usando {n} términos: {aproximacion}")
print(f"Valor real de e^{x}: {valor_real}")
print(f"Diferencia: {abs(valor_real - aproximacion)}")
