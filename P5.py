# Solicitar ingresar la potencia n
n = int(input("Ingrese el valor de n para calcular 2 elevado a la potencia n: "))
# Inicializar el resultado de la potencia
resultado = 1
# Utilizar un ciclo for para calcular 2**n
for _ in range(n):
    resultado *= 2
# Imprimir resultado
print(f"2 elevado a la potencia {n} es {resultado}")
