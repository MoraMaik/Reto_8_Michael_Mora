# Definir la función para calcular el factorial de un número
def calcular_factorial(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial
# Solicitar al usuario que ingrese el número natural n
n = int(input("Ingrese un número natural n: "))
# Verificar que el número ingresado sea un número natural (n >= 1)
if n < 1:
    print("Por favor, ingrese un número natural mayor o igual a 1.")
else:
    # Imprimir los números de 1 a n con su respectivo factorial
    for numero in range(1, n + 1):
        factorial = calcular_factorial(numero)
        print(f"{numero}! = {factorial}")
