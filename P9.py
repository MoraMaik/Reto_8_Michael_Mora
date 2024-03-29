import math

# Definir la función para calcular la aproximación de seno(x)
def aproximar_seno(x, n):
    suma = 0.0  # iniciar la suma de la serie
    # Sumar los términos de la serie
    for i in range(n):
        # Calcular el término i de la serie
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        suma += termino
    return suma
# Solicitarel valor de x
x = float(input("Ingrese el valor de x para calcular sen(x): "))
# Solicitar el número de términos de la serie
n = int(input("Ingrese el número de términos n para la aproximación: "))
# Calcular su aproximación
aproximacion = aproximar_seno(x, n)
# Calcular su valor real usando math.sin
valor_real = math.sin(x)
# Mostrar la aproximación y la diferencia con el valor real
print(f"Aproximación de sen({x}) usando {n} términos: {aproximacion}")
print(f"Valor real de sen({x}): {valor_real}")
print(f"Diferencia: {abs(valor_real - aproximacion)}")
