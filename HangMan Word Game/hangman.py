#replica of hangman word game
import random
from hangmanwords import word_list
from Hangmanart import stages, logo
print(logo)
computerchoice = random.choice(word_list)
print(computerchoice)
lives = 6  #total lives
display = []

for _ in range(len(computerchoice)):
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess = input("guess one word").lower()
    print("your gussed word is :" , guess)
    if guess in display:
        print("you have already gussed this letter")
    for position in range(len(computerchoice)):
        letter = computerchoice[position]
        if letter == guess:
            display[position] = letter

    #for the wrong guessess lives will decrease
    if guess not in computerchoice:
        lives -= 1
        print(f"your gussed word {guess} is not in the box")
        print("you have lost one life")
        if lives == 0:
            end_of_game = True
            print("you lose")
    print(f"{' '.join(display)}")
    print(display)


    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])


