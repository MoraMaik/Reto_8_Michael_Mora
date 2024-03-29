# Solicitar que se ingrese el número natural n
n = int(input("Ingrese un número natural n (n ≥ 2): "))
# Ajustar n al par más cercano menor o igual que n
if n % 2 != 0:
    n -= 1
# Imprimir números pares en forma descendente hasta 2
for numero in range(n, 1, -2):
    print(numero)
