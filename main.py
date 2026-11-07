#!/usr/bin/env python3
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
