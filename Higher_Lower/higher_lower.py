from art import logo
print(logo)
from game_data import data
import random
result = ""
guess_game = True
score = 0
while guess_game:
    item1 = random.choice(data)
    item1_name = item1["name"]
    item1_desc = item1["description"]
    item1_count = item1["country"]



    print(f"Compare A :{item1_name},{item1_desc},{item1_count}")

    from art import vs
    print(vs)


    item2 = random.choice(data)
    item2_name = item2["name"]
    item2_desc = item2["description"]
    item2_count = item2["country"]
    print(f"Compare B : {item2_name},{item2_desc},{item2_count}")
    guess = (input("who has more followers?A or B : ")).capitalize()


    if item1["follower_count"] > item2["follower_count"]:
        result ="A"
    elif item2["follower_count"] > item1["follower_count"]:
        result = "B"

    elif item2["follower_count"] == item1["follower_count"]:
        result = "same"

    if result =="A" and guess == "A":
        print("correct guess: ")
        score += 1
        print(f"ur current score: {score}")

    elif result =="B" and guess == "B":
        item2 = random.choice(data)
        print("correct guess: ")
        score += 1
        print(f"ur current score: {score}")

    elif result == "same":
        print("sorry error occured, restart game again")

    else:
        print("wrong guess")
        print(f"ur final score is: {score}")
        guess_game = False

