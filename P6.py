# Leer el número NATURAL n
n = int(input("Ingrese el valor de n (potencia): "))
# Leer el dato de tipo real x
x = float(input("Ingrese el valor de x (base): "))
# Inicializar el resultado de la potencia
resultado = 1.0
# Utilizar un ciclo for para calcular x**n
for _ in range(n):
    resultado *= x
# Imprimir el resultado
print(f"{x} elevado a la potencia {n} es {resultado}")
