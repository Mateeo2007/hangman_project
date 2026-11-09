#!/usr/bin/env python3
# -*- coding: cp1252 -*-
"""
Codigo principal del juego,
acaÃ ¡se ejecuta lo que va a ver el usuio, se define
la funcioÃn que obtiene letras valids y
importa el resto de funciones para poder
ejecutar el juego correctamente.
"""
from utils import get_random_word
from game import HangmanGame  # tarea 5


def obtener_letra_valida(letras_adivinadas):
    while True:
        letra = input("Ingresa¡ una letra: ").strip().lower()

        if len(letra) != 1:
            print("Error: Tene©s que ingresar una sola letra.")
        elif not letra.isalpha():
            print("Error: El ingreso debe ser una letra.")
        elif letra in letras_adivinadas:
            print("Ya ingresaste esa letra. Proba¡ con otra.")
        else:
            return letra


def main():  # esta es la funciÃn principal, aca ejecuta el juego
    palabrajuego = get_random_word()

    juego = HangmanGame(palabrajuego)

    print("Juego del ahorcado.")

    while juego.errors < juego.max_errors:

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


if __name__ == "__main__":
    main()
