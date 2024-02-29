import random

def hangman():

  print("Привет! Добро пожаловать в игру Виселица!")

  wordlist = ["мандарин", "яблоко", "груша", "виноград", "апельсин", "манго"]
  secret = random.choice(wordlist)
  guesses = "ауоыиэяюёе"
  turns = 5

  while turns > 0:
    missed = 0

    for letter in secret:
      if letter in guesses:
        print(letter, end=" ")
      else:
        print("_", end=" ")
        missed += 1
    if missed == 0:
      print("\nТы выиграл!")
      break
    guess = input("\nНазови букву: ")
    guesses += guess

    if guess not in secret:
      turns -= 1
      print("\nНе угадал.")

    print("\n", "Осталось попыток: ", turns)

    if turns == 0:
      print("\n\nЭто слово: ", secret)

  ans = "да"
  while ans == "да":
    hangman()
  print("Спасибо за игру!")


hangman()
