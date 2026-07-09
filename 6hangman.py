import random

stages = [
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
totallen = len(chosen_word)
placeholder = ["_"] * totallen

lifeline = 6
guessedword = []


while lifeline > 0 and "_" in placeholder:
    placeholderstr = "".join(placeholder)
    print(f"Guess word :{placeholderstr}")
    guess = input("Guess a letter : ").lower()
    if guess in guessedword:
        print(f"You already guessed :{guess}.\nGuess another word ")
    else:
        guessedword.append(guess)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue
        if guess in chosen_word:
            for i in range(0, totallen):
                if chosen_word[i] == guess:
                    placeholder[i] = guess

        else:
            print(f"'{guess}' is not there ")
            lifeline -= 1
            print(f"{stages[lifeline]}")
            print(f"lifeline:{lifeline}/6")


if "_" not in placeholder:
    print("You won")
else:

    print("You loose")
    print(f"The correct word in {chosen_word}")
