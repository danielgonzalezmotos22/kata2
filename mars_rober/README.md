# Introducción
La agencia espacial te ha encargado el software de navegación del nuevo Rover. En esta fase, el objetivo es establecer la comunicación básica: que el robot entienda dónde está y cómo girar o avanzar.

# Iteracion 1
## Entidades Iniciales
Para esta primera iteración, trabajarás principalmente con dos conceptos:
### El Rover: Un objeto que mantiene su estado (X, Y, Dirección).
### Los Comandos: Una secuencia de letras que el Rover debe procesar.
Movimiento y Rotación en Plano Infinito
En esta etapa, Marte es un plano infinito (sin bordes). El Rover debe procesar comandos simples: f (adelante), b (atrás), l (izquierda) y r (derecha).

Posicion inicial va a ser 0,0,N