# Program to display position of letter in the random word

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

print(display)
