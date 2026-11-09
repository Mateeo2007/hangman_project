#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""
Codigo principal del juego,
acá se ejecuta lo que va a ver el usuario, se define
la función que obtiene letras válidas y
importa el resto de funciones para poder
ejecutar el juego correctamente.
"""
from utils import get_random_word
from game import HangmanGame  # tarea 5


def obtener_letra_valida(letras_adivinadas):
    while True:
        letra = input("Ingresá una letra: ").strip().lower()

        if len(letra) != 1:
            print("Error: Tenés que ingresar una sola letra.")
        elif not letra.isalpha():
            print("Error: El ingreso debe ser una letra.")
        elif letra in letras_adivinadas:
            print("Ya ingresaste esa letra. Probá con otra.")
        else:
            return letra


def main():  # esta es la función principal, acá ejecuta el juego
    palabrajuego = get_random_word()

    juego = HangmanGame(palabrajuego)

    print("Juego del ahorcado.")

    while not juego.is_won() and not juego.is_lost():

        print("Progreso: ", juego.display_progress())

        print("Letras ya usadas: ", juego.guessed_letters)

        intentos_restantes = juego.max_errors - juego.errors
        print(f"Intentos incorrectos restantes: {intentos_restantes}")

        letra = obtener_letra_valida(juego.guessed_letters)

        acierto = juego.process_guess(letra)

        if acierto:
            print(f"Correcto, la letra '{letra}' existe en la palabra")
        else:
            print(f"Incorrecto, la letra '{letra}' no existe en la palabra")

    if juego.is_won():
        print("¡Ganaste!")
    else:
        print("Fin del juego")


if __name__ == "__main__":
    main()
