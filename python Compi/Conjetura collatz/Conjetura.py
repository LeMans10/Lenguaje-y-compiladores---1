def verificar_collatz(p, q):
    # regla para demostración
    if q < 100 * p:
        return f"Error: No se cumple la regla q >= 100p (q={q}, 100p={100 * p})"

    print(f"Verificando el intervalo [{p}, {q}]...\n")

    # iterar sobre cada número n en el rango [p, q]
    for n in range(p, q + 1):
        original_n = n
        secuencia = [str(n)]

        # Reglas de la congetrua
        while n > 1:
            if n % 2 == 0:  # par
                n = n // 2
            else:
                n = 3 * n + 1  # impar
            secuencia.append(str(n))

        # Imprimir secuencia de cada número para demostrar el proceso
        print(f"n={original_n}: {' -> '.join(secuencia)}")

    return "\nConjetura de Collatz demostrada en el intervalo."


# ejecución
try:
    p = int(input("Ingrese el valor de p: "))
    q = int(input("Ingrese el valor de q: "))

    resultado = verificar_collatz(p, q)
    print(resultado)
except ValueError:  # excepción porque n debe ser un entero positivo
    print("ingrese solo números enteros.")
