

import random

num = random.randint(1,100)
tries = 0

user = input("Enter your name: ")
user = user.strip()

print(f"Hello {user}")
print("WOuld you like to play a game")
print("1) Yes")
print("2) No")

option = int(input("Select your option: "))

if option == 1:
    print("Im thinking a number between 1-100")
    print(" You have three tries")

    guess = input("Guess a number: ")
    guess = int(guess)
    tries +=1

    if guess>num:
        print("guess lower ")
    elif guess<num:
        print("guess higher")

    while guess != num and tries < 3:
        guess = input("Try again")
        guess = int(guess)
        tries += 1

        if guess > num:
            print("guess lower ")
        elif guess < num:
            print("guess higher")

    if guess == num:
        print(f"you won!\n Number of tries: {tries}")
    else:
        print("You lost")
elif option == 2:
    print("Thank you")
else:
    print("Invalid Option")
