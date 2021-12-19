# Importo las librerías necesarias para la resolución del ejercicio.
import turtle


def estrella(puntas, lado=200):
    # Sobre esta función voy a desarollar el ejercicio.
    # Para calcular el ángulo necesitamos primero hallar el mcd entre dos números enteros.
    def mcd(a, b):
        div = 0
        top = min(abs(a), abs(b))
        for n in range(1, top + 1):
            if a % n == 0 and b % n == 0:
                div = n
        return div

    # Antes de continuar desarrollando la función hago referencia a que tiene que tener más de 4 puntas.
    if puntas <= 4:
        print(
            "El número de puntas introducido es insuficiente para trazar correctamente la estrella."
        )
        return
    for n in range(puntas // 2, 1, -1):
        # Vamos a comprobar que n y el número de puntas son coprimos.
        if mcd(puntas, n) == 1:
            alfa = 360 / puntas * n
            break
    # Ahora vamos a trazar la estrella empleando toda la información anterior.
    for _ in range(puntas):
        # Trazamos el lado.
        turtle.forward(lado)
        # Rotamos con el ángulo correspondiente.
        turtle.left(alfa)

    return


estrella(
    int(
        input(
            "Introduzca el número de puntas que desea que tenga su estrella(mayor que 4): "
        )
    )
)
input("Pulse la tecla Enter para cerrar la ventana: ")
