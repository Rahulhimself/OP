# from art import logo
# print(logo)
# from game_data import data
# import random
# result = ""
# guess_game = True
# score = 0
# while guess_game:
#     item1 = random.choice(data)
#     item1_name = item1["name"]
#     item1_desc = item1["description"]
#     item1_count = item1["country"]
#
#
#
#     print(f"Compare A :{item1_name},{item1_desc},{item1_count}")
#
#     from art import vs
#     print(vs)
#
#
#     item2 = random.choice(data)
#     item2_name = item2["name"]
#     item2_desc = item2["description"]
#     item2_count = item2["country"]
#     print(f"Compare B : {item2_name},{item2_desc},{item2_count}")
#     guess = (input("who has more followers?A or B : ")).capitalize()
#
#
#     if item1["follower_count"] > item2["follower_count"]:
#         result ="A"
#     elif item2["follower_count"] > item1["follower_count"]:
#         result = "B"
#
#     elif item2["follower_count"] == item1["follower_count"]:
#         result = "same"
#
#     if result =="A" and guess == "A":
#         print("correct guess: ")
#         score += 1
#         print(f"ur current score: {score}")
#
#
#     elif result =="B" and guess == "B":
#         item2 = random.choice(data)
#         print("correct guess: ")
#         score += 1
#         print(f"ur current score: {score}")
#
#     elif result == "same":
#         print("sorry error occured, restart game again")
#
#     else:
#         print("wrong guess")
#         print(f"ur final score is: {score}")
#         guess_game = False
#


import random

# from replit import clear

from art import logo, vs
from game_data import data


def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()










