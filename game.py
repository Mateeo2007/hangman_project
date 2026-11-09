#!/usr/bin/env python3

class HangmanGame:
    """Representa el estado de una partida de ahorcado."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra las letras descubiertas y oculta las restantes."""
        progress = []

        for letter in self.word:
            if not letter.isalpha() or letter.lower() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        return " ".join(progress)
    def process_guess(self, letter): #tarea 4
        if letter in self.word:
            self.guessed_letters.append(letter) # si la letra est√°en la palabra, la a√ade a las letras adivinadas y retorna true, si no, suma un error y retorna falso.
            return True
        else:
            self.errors += 1
            return False
