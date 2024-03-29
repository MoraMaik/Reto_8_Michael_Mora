# Utilizar ciclos for anidados para generar las tablas de multiplicar del 1 al 9
for numero_tabla in range(1, 10):
    print(f"Tabla del {numero_tabla}:")
    for multiplicador in range(1, 11):
        resultado = numero_tabla * multiplicador
        print(f"{numero_tabla} x {multiplicador} = {resultado}")
    # Imprimir una línea en blanco como separador entre tablas para se lea bien
    print("")
