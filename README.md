# Reto_8_Michael_Mora
Desarrollo reto 8, segun lo aprendido en [Clase 11](http://https://github.com/fegonzalez7/pdc_unal_clase11 "Clase 11"), con las siguientes recomendaciones:

Desarrolle la mayoria de ejercicios en clase. Para cada punto cree un programa individual asimismo cree un notebook con la solucion a todos los problemas. Al finalizar suba todo a un repo y subalo al canal reto_8 en slack, para ellos se dispondra de un listado donde debe pegar el enlace al repo (misma dinamica que con el taller 1).

**Nota:** Todo el codigo de aqui en adelante debe ir debidamente documentado.
_______________________________
## **Punto 1**

**Instrucciones:** Imprimir un listado con los numeros del 1 al 100 cada uno con su respectivo cuadrado.
```python
# Usar un ciclo for junto con una coleccion de rango para iterar del 1 al 100
for numero in range(1, 101):
    # Imprimir el numero y su cuadrado
    print(f"{numero} - {numero**2}")
```
En este codigo, la variable condicion se establece en `False`, lo que hace que la condicion del ciclo `while` tambien sea `False` desde el principio. Como resultado, el cuerpo del ciclo nunca se ejecuta, y el programa continua su ejecucion con cualquier codigo que se escriba despues del ciclo.

_______________________________
## **Punto 2**

**Instrucciones:** Imprimir un listado con los numeros impares desde 1 hasta 999 y seguidamente otro listado con los numeros pares desde 2 hasta 1000.
```python
# Imprimir números impares desde 1 hasta 999
print("Números impares del 1 al 999:")
for numero_impar in range(1, 1000, 2):
    print(numero_impar)
# Separador para hacer la salida más clara
print("\nNúmeros pares del 2 al 1000:")
# Imprimir números pares desde 2 hasta 1000
for numero_par in range(2, 1001, 2):
    print(numero_par)
```
Este codigo utiliza dos ciclos `for`:

+ El primer ciclo `for` itera sobre un rango de numeros impares generado por `range(1, 1000, 2)`. La funcion `range` aqui comienza en 1, termina antes de 1000, e incrementa el contador en 2 en cada paso, generando asi todos los numeros impares dentro del rango especificado.

+ El segundo ciclo for hace lo propio para los numeros pares, utilizando `range(2, 1001, 2)`. Este rango comienza en 2 y va hasta 1000 (inclusive, por eso se usa 1001 como limite superior), incrementando tambien en 2 para asegurar que solo se generen numeros pares.
_______________________________
## **Punto 3**

**Instrucciones:** Imprimir los numeros pares en forma descendente hasta 2 que son menores o iguales a un numero natural n ≥ 2 dado
```python
# Solicitar que se ingrese el número natural n
n = int(input("Ingrese un número natural n (n ≥ 2): "))
# Ajustar n al par más cercano menor o igual que n
if n % 2 != 0:
    n -= 1
# Imprimir números pares en forma descendente hasta 2
for numero in range(n, 1, -2):
    print(numero)
```
Este codigo inicia pidiendo al usuario que ingrese un numero natural `n`, con la condicion de que `n≥2`. Luego, ajusta `n` al numero par mas cercano menor o igual a `n` si n es impar, para asegurarnos de comenzar con un numero par. Finalmente, utiliza un ciclo `for` con una coleccion de rango que empieza en `n`, termina antes de 2 (es decir, no incluye el numero 1), y tiene un paso de −2, lo que significa que decrece de 2 en 2, generando asi todos los numeros pares en orden descendente desde `n` hasta 2.

_______________________________
## **Punto 4**

**Instrucciones:** Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
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
```
_______________________________
## **Punto 5**

**Instrucciones:** Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
# Solicitar ingresar la potencia n
n = int(input("Ingrese el valor de n para calcular 2 elevado a la potencia n: "))
# Inicializar el resultado de la potencia
resultado = 1
# Utilizar un ciclo for para calcular 2**n
for _ in range(n):
    resultado *= 2
# Imprimir resultado
print(f"2 elevado a la potencia {n} es {resultado}")
```
Este código empieza solicitando al usuario el valor de `n`, luego inicializa una variable `resultado` en  1 (ya que cualquier número elevado a la 0 es 1, y este valor servirá como el acumulador en el que se multiplicará 2 sucesivamente). Utilizo un ciclo `for` que itera `n` veces, multiplicando el resultado por 2 en cada iteración.

_______________________________
## **Punto 6**

**Instrucciones:** Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
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
```
_______________________________
## **Punto 7**

**Instrucciones:** Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
# Utilizar ciclos for anidados para generar las tablas de multiplicar del 1 al 9
for numero_tabla in range(1, 10):
    print(f"Tabla del {numero_tabla}:")
    for multiplicador in range(1, 11):
        resultado = numero_tabla * multiplicador
        print(f"{numero_tabla} x {multiplicador} = {resultado}")
    # Imprimir una línea en blanco como separador entre tablas para se lea bien
    print("")
```

_______________________________
## **Punto 8**

**Instrucciones:** 

[![Whats-App-Image-2024-03-28-at-7-19-30-PM.jpg](https://i.postimg.cc/ncS5x99F/Whats-App-Image-2024-03-28-at-7-19-30-PM.jpg)](https://postimg.cc/9rT1tMBK)

```python
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
```
Mi código importa el módulo `math` para utilizar `math.exp` para calcular el valor real de `e**x` y `math.factorial` para calcular los factoriales en la serie de Maclaurin. La función `aproximar_exponencial` realiza la sumatoria de los primeros `n` términos de la serie para calcular la aproximación de  `e**x` . Finalmente, el programa solicita al usuario el valor de `x` y el número de términos `n`, calcula la aproximación y la compara con el valor real, imprimiendo la diferencia.

_______________________________
## **Punto 9**

**Instrucciones:** 

[![Whats-App-Image-2024-03-28-at-7-28-25-PM.jpg](https://i.postimg.cc/Mp7Wd8GJ/Whats-App-Image-2024-03-28-at-7-28-25-PM.jpg)](https://postimg.cc/v4mFZk90)

```python
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
```

el código define una función `aproximar_seno` que calcula una sumatoria de los términos de la serie de Maclaurin para la función `seno`. La serie alterna los signos y utiliza factoriales de números impares, lo que se refleja en la fórmula `((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)` . Luego, solicita al usuario que ingrese el valor de `x` y el número de términos `n` y calcula la aproximación y el valor real de `seno(x)` usando `math.sin`. Finalmente, muestra la aproximación y la diferencia entre el valor real y la aproximación.

_______________________________
## **Punto 10**

**Instrucciones:** 

[![Whats-App-Image-2024-03-28-at-7-28-25-PM.jpg](https://i.postimg.cc/Mp7Wd8GJ/Whats-App-Image-2024-03-28-at-7-28-25-PM.jpg)](https://postimg.cc/v4mFZk90)

**DISCLAIMER**: Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.


```python
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
```

este código define una función `aproximar_arctan` que calcula la sumatoria de los términos de la serie de Maclaurin para la función `arcotangente`. También define una función `determinar_n_para_error_minimo` que itera incrementando `n` hasta que la diferencia entre la aproximación y el valor real es menor que el error permitido. Después de obtener el valor de `x` solitado y verificar que esté en el rango permitido, el programa calcula y muestra la aproximación, el valor real y la diferencia entre ellos.
_______________________________
FIN RETO.
