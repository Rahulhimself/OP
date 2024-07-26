import random
no_of_letters = int(input("welcome to password generator,\nfirstly how many letters do you want in your password? :"))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","%","^","&","$","*"]
password = []

for lett in range(1, no_of_letters + 1):
    password.append(random.choice(letters))
print(password)
no_of_numbers = int(input("how many numbers you want? :"))
for numb in range(1, no_of_numbers + 1):
    password.append(random.choice(numbers))
print(password)
no_of_symbols = int(input("how many symboles you want? :"))
for sym in range(1, no_of_symbols + 1):
    password.append(random.choice(symbols))
print("your'e unique password is : ",password)
random.shuffle(password)
print(password)
new_password=""
for char in password:
    new_password += char
print("final passcode is", new_password)



