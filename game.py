"""task_1.py"""


import random


class Hangman:
    """Класс виселицы"""

    def __init__(self):
        self.wordlist = ["мандарин", "яблоко",
                         "груша", "виноград", "апельсин", "манго"]
        self.secret = random.choice(self.wordlist)
        self.guesses = "ауоыиэяюёе"
        self.turns = 5

    def display_word(self):
        """Метод показания слова"""
        for letter in self.secret:
            if letter in self.guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")

    def play(self):
        """Метод логики игры"""
        print("Добро пожаловать в игру Виселица!")

        while self.turns > 0:
            self.display_word()
            missed = 0

            for letter in self.secret:
                if letter not in self.guesses:
                    missed += 1

            if missed == 0:
                print("\nТы выиграл")
                break

            guess = input("\nНазови букву: ")
            self.guesses += guess

            if guess not in self.secret:
                self.turns -= 1
                print("\nНе угадал.")

            print("\nОсталось попыток:", self.turns)

            if self.turns == 0:
                print("\n\nЭто слово:", self.secret)
                break

        self.play_again()

    def play_again(self):
        """метод повторной попытки"""
        answer = input("Хочешь сыграть ещё раз? (да/нет): ")
        if answer.lower() == "да":
            new_game = Hangman()
            new_game.play()
        else:
            print("Спасибо за игру!")


if __name__ == "__main__":
    game = Hangman()
    game.play()
