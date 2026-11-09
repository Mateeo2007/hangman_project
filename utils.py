#!/usr/bin/env python3
def get_random_word():
    import random
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lista = []
    for n in lines:
        linea = n.strip()
        if linea:
            lista.append(linea)
    return random.choice(lista)
