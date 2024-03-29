import math

# Defini una función para calcular la aproximación de arctan(x)
def aproximar_arctan(x, n):
    suma = 0.0  # Inicia la suma de la serie
    # Suma los términos de la serie de Maclaurin
    for i in range(n):
        # Calcula el término i de la serie
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        suma += termino
    return suma
# Determina n para un error menor al 0.1%
def determinar_n_para_error_minimo(x, error_permitido=0.001):
    n = 0
    while True:
        aproximacion = aproximar_arctan(x, n)
        valor_real = math.atan(x)
        error_actual = abs(valor_real - aproximacion)
        if error_actual < error_permitido:
            return n
        n += 1
# Solicitar el valor de x
x = float(input("Ingrese el valor de x para calcular arctan(x) (debe estar entre -1 y 1): "))
# Verificar que x esté en el rango permitido
if x < -1 or x > 1:
    print("El valor ingresado para x está fuera del rango permitido.")
else:
    # Calcular n para el error menor al 0.1%
    n = determinar_n_para_error_minimo(x)
    # Calcular la aproximación
    aproximacion = aproximar_arctan(x, n)
    # Calcular el valor real usando math.atan
    valor_real = math.atan(x)
    # Mostrar la aproximación, el valor real y la diferencia
    print(f"Aproximación de arctan({x}) usando {n} términos: {aproximacion}")
    print(f"Valor real de arctan({x}): {valor_real}")
    print(f"Diferencia: {abs(valor_real - aproximacion)}")
