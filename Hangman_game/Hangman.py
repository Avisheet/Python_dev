#!/usr/bin/env python3

import logo
import hangman_list
import random

stages = logo.stages

end_of_game = False
word_list = hangman_list.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(stages[lives])

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"Correct word was: {chosen_word}")
            
    print(f"{' '.join(display)}")
    
    
    if "_" not in display:
        end_of_game = True
        print("You win <3")

