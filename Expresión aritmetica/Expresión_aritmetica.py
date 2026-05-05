import re


def analizar_expresion(cadena):
    # definicion de los regex
    patrones = [
        ("NUMERO", r"\d+(\.\d+)?"),
        ("OPERANDO", r"[a-zA-Z][a-zA-Z0-9]*"),
        ("OPERADOR", r"[\+\-\*/]"),
        ("PAREN_IZQ", r"\("),
        ("PAREN_DER", r"\)"),
        ("ESPACIO", r"\s+"),
    ]

    regex_completa = "|".join(f"(?P<{nombre}>{patron})" for nombre, patron in patrones)

    tokens_encontrados = []
    balance_parentesis = 0
    error_detectado = False

    # buscar coincidencias
    for coincidencia in re.finditer(regex_completa, cadena):
        tipo = coincidencia.lastgroup
        valor = coincidencia.group(tipo)

        if tipo == "ESPACIO":
            continue
        elif tipo == "PAREN_IZQ":
            balance_parentesis += 1
        elif tipo == "PAREN_DER":
            balance_parentesis -= 1

        # si en algún punto hay más de cierre que de apertura
        if balance_parentesis < 0:
            error_detectado = True

        tokens_encontrados.append(f"{tipo} {valor}")

    # verificar caracteres no reconocidos (ERROR)
    limpieza = re.sub(regex_completa, "", cadena)
    if limpieza.strip():
        tokens_encontrados.append(f"ERROR {limpieza.strip()}")

    # Formatear salida
    resultado = " ".join(tokens_encontrados)

    # Verificación final de balance
    if balance_parentesis == 0 and not error_detectado:
        resultado += " PARÉNTESIS BALANCEADOS."
    else:
        resultado += " PARÉNTESIS NO BALANCEADOS."

    return resultado


# cadena expresión aritmetica
C = input("Ingrese una expresión aritmética: ")
print(f"Entrada: {C}")
print(f"Salida:\n{analizar_expresion(C)}")
