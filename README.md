<h1 align="center">Las Estrellas Regulares</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---

En este [repositorio](https://github.com/jmedina28/Las-Estrellas-Regulares) queda resuelto el programa que te devuelve una estrella de n puntas que tu introduzcas en consola. 

***
## Índice
1. [Introducción](#id1)
3. [Diagrama de flujo](#id2)
3. [Código](#id3)
4. [Resultado](#id4)

***

## 1. Introducción<a name="id1"></a>

El ejercicio consiste en programar una función que dibuje estrellas como la que aparece a continuación con un número de puntas que introduce el usuario.

<br>
<img height="250" src="https://github.com/jmedina28/Las-Estrellas-Regulares/blob/0f3423778431242efc6cf1f9a708549665b1fddb/estrella.png" />
<br>

Para ello voy a utilizar el módulo de Python Turtle que permite realizar trazos sencillos en una ventana gráfica. 

Para documentarme acerca de cómo usar el módulo Turtle he usado el siguiente resumen:

- [Resumen](https://docs.python.org/es/3.9/library/turtle.html)

## 2. Diagrama de flujo<a name="id2"></a>
El diagrama de flujo es el siguiente:

<br>
<img height="450" src="https://github.com/jmedina28/Las-Estrellas-Regulares/blob/ebae8d1cf1a3cdc19e336bbb307ac8271a3062d1/flowchart.jpg" />
<br>


## 3. Código<a name="id3"></a>
```python
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


# Ejecutamos la función que va a generar nuestra estrella de n puntas:
estrella(
    int(
        input(
            "Introduzca el número de puntas que desea que tenga su estrella(mayor que 4): "
        )
    )
)
# Introduzco este input para que no se cierre la ventana de golpe al acabar de trazar la estrella.
input("Pulse la tecla Enter para cerrar la ventana: ")
  ```
## 4. Resultado<a name="id4"></a>

- Entrada:

<br>
<img height="60" src="https://github.com/jmedina28/Las-Estrellas-Regulares/blob/0f3423778431242efc6cf1f9a708549665b1fddb/Consola.PNG" />
<br>

- Salida:

<br>
<img height="250" src="https://github.com/jmedina28/Las-Estrellas-Regulares/blob/0f3423778431242efc6cf1f9a708549665b1fddb/estrellaturtle.PNG" />
<br>

- Error(cuando introduces un número de puntas menor o igual que 4):

<br>
<img height="70" src="https://github.com/jmedina28/Las-Estrellas-Regulares/blob/8d9b4a68add7d4ce8cd0e48209c4775081da7ea3/casopuntas.PNG" />
<br>

