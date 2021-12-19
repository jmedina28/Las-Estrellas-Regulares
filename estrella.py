# Importo las librerías necesarias para la resolución del ejercicio.
import turtle


def estrella():
    # Sobre esta función voy a desarollar el ejercicio.
    # Para calcular el ángulo necesitamos primero hallar el mcd entre dos números enteros.
    def mcd(a, b):
        div = 0
        top = min(abs(a), abs(b))
        for n in range(1, top + 1):
            if a % n == 0 and b % n == 0:
                div = n
        return div

    print(mcd(5, 25))


estrella()
