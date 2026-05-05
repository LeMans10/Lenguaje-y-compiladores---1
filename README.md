## Autor
**Mansour Ortega**

---

# Actividad lenguajes y compiladores

He desarrollado algoritmos para resolver los problemas planteados haciendo uso principalmente de validaciones de tipo RegEx y ElseIF en el lenguaje python

## Contenido

1.  **Analizador de expresiones aritméticas**
2.  **Validador de notación FEN)**
3.  **Verificador de la Conjetura de Collatz**

---

## Descripción de los Problemas

### 1. Analizador de expresiones
El programa recibe una cadena de texto (expresión aritmética) y la descompone en sus componentes mínimos según las siguientes reglas:
*   **NUMERO**: Enteros o reales (ej: `12`, `3.14`).
*   **OPERADOR**: `+`, `-`, `*`, `/`.
*   **OPERANDO**: Variables que inician con letra (ej: `VALOR`, `A`).
*   **PARÉNTESIS**: Clasifica apertura y cierre, verificando además que el balance sea correcto.

### 2. Validador FEN
Valida si una cadena representa una posición legal de ajedrez bajo la Notación Forsyth-Edwards. 
*   **Piezas**: `P` (Pawn), `K` (Knight), `B` (Bishop), `R` (rook), `Q` (Queen), `K` (King).
*   **Validación lógica**: Comprueba que cada una de las 8 filas del tablero sume exactamente 8 casillas (contando piezas y espacios vacíos).
*   **Campos adicionales**: Valida turno, derechos de enroque y captura al paso.

### 3. Conjetura de Collatz
Algoritmo que aplica la secuencia de Collatz a todos los números en un intervalo $[p, q]$.
*   **Regla**: Si $n$ es par $\rightarrow n/2$; si es impar $\rightarrow 3n + 1$.
*   **Restricción**: El programa para efectos demostrativos solo se ejecuta si el límite superior es al menos 100 veces el inferior ($q \geq 100p$).

---

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/LeMans10/Lenguaje-y-compiladores---1/
   cd [ubicación del repositorio]

2. **Dependencias:**
   
    tener python instalado en el ordenador (https://www.python.org/downloads/)
   
3. **Ejecución:**

    basta con acceder a cada carpeta con el comando "cd" en la terminal desde la carpeta del repositorio y ejecutar el archivo .py con python
    ejemplo:
    ```bash
    cd "Cadena C FEN"
    py cadena_FEN.py
  
