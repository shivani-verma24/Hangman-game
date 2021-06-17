import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

list1 = []
lives = 6
for i in range(word_length):
    list1 += "_"

while ("_" in list1):
    guess = input("Guess a letter: ").lower()

    if (guess in list1):
        print(f"Already guessed '{guess}', guess another letter.")
        continue

    for i in range(word_length):
        if (chosen_word[i] == guess):
            list1[i] = guess

    if guess not in chosen_word:
        print(f"'{guess}' is not in the chosen word. You lose a life.")
        print(stages[lives])
        lives -= 1
        if (lives == -1):
            break

    print(" ".join(list1))

final_word = "".join(list1)
if (final_word == chosen_word):
    print(final_word)
    print("You won!")
else:
    print(f"Word was '{chosen_word}'")
    print("You lose.")

# Project by Shivani Verma
