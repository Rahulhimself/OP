#replica of hangman word game
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = ["smartphone", "newone", "hangman"]
import random
computerchoice = random.choice(words)
lives = 6
print(computerchoice)
display = []
for _ in range(len(computerchoice)):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess one word").lower()
    print("yor're gussed word is :" , guess)
    for position in range(len(computerchoice)):
        letter = computerchoice[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")


