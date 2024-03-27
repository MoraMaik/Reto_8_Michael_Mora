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
# Imprimir numeros impares desde 1 hasta 999
print("Numeros impares del 1 al 999:")
for numero_impar in range(1, 1000, 2):
    print(numero_impar)
# Separador para hacer la salida mas clara
print("\nNumeros pares del 2 al 1000:")
# Imprimir numeros pares desde 2 hasta 1000
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
# Solicitar al usuario que ingrese el numero natural n
n = int(input("Ingrese un numero natural n (n ≥ 2): "))
# Ajustar n al par mas cercano menor o igual que n
if n % 2 != 0:
    n -= 1
# Imprimir numeros pares en forma descendente hasta 2
for numero in range(n, 1, -2):
    print(numero)
```
Este codigo inicia pidiendo al usuario que ingrese un numero natural `n`, con la condicion de que `n≥2`. Luego, ajusta `n` al numero par mas cercano menor o igual a `n` si n es impar, para asegurarnos de comenzar con un numero par. Finalmente, utiliza un ciclo `for` con una coleccion de rango que empieza en `n`, termina antes de 2 (es decir, no incluye el numero 1), y tiene un paso de −2, lo que significa que decrece de 2 en 2, generando asi todos los numeros pares en orden descendente desde `n` hasta 2.

_______________________________
## **Punto 4**

**Instrucciones:** Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
