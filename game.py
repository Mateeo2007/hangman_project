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

    def process_guess(self, letter):  # tarea 4
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.guessed_letters.append(letter)
            self.errors += 1
            return False

    def is_won(self):
        """Comprueba si se adivinaron todas las letras de la película."""
        return all(
            not letter.isalpha() or letter.lower() in self.guessed_letters
            for letter in self.word
        )

    def is_lost(self):
        """Comprueba si se alcanzó el máximo de errores permitidos."""
        return self.errors >= self.max_errors