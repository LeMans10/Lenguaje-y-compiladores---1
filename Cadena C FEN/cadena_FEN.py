import re


def validar_fen(fen):
    # Definimos las regex para FEN
    piezas_regex = r"([pnbrqkPNBRQK1-8]{1,8}/){7}[pnbrqkPNBRQK1-8]{1,8}"
    turno_regex = r"[wb]"
    enroque_regex = r"(K?Q?k?q?|-)"
    al_paso_regex = r"([a-h][36]|-)"
    reloj_regex = r"\d+"
    jugada_regex = r"\d+"

    # Unimos todo en un patrón con espacios
    fen_completo = f"^{piezas_regex} {turno_regex} {enroque_regex} {al_paso_regex} {reloj_regex} {jugada_regex}$"

    if re.match(fen_completo, fen):
        # validación de filas de 8 casillas
        filas = fen.split(" ")[0].split("/")
        for fila in filas:
            suma_casillas = 0
            for char in fila:
                if char.isdigit():
                    suma_casillas += int(char)
                else:
                    suma_casillas += 1
            if suma_casillas != 8:
                return "ERROR: Una de las filas no tiene 8 casillas."

        return "NOTACIÓN FEN VÁLIDA"
    else:
        return "NOTACIÓN FEN INVÁLIDA (Error de formato)"


# Cadena C
c = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
print(f"Resultado: {validar_fen(c)}")
