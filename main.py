#Step 1 
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = list(random.choice(word_list))
lives = 6
end_of_game = False
display = []

print(logo)
print("Try to beat the computer.\nYou have 6 lives, good luck!\n")

while len(display) < len(chosen_word):
    display.append("_")

while "_" in display:
    
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")
    print(f"Number of lives: {lives} \n {stages[lives]}")
    print(display)

end_of_game = True
print("You win !!!")


