import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

chosen_word = list(random.choice(word_list))
lives = 6
end_of_game = False
display = []

print(logo)
print("Try to beat the computer.\nYou have 6 lives, good luck!\n")

while len(display) < len(chosen_word):
    display.append("_")

while "_" in display:
    
    guess = input("Guess a letter: \n").lower()
    clear()
    
    if guess in display:
        print(f"You have already guess {guess}")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word to guess ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")
    print(f"Number of lives: {lives} \n {stages[lives]}")
    print(f"{' '.join(display)}")

end_of_game = True
print("You win !!!")


