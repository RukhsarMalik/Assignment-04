#guess my number game

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Enter an integer from 1 to 100: "))
    if guess < number:
        print("Your guess is low")
    elif guess > number:
        print("Your guess is high")
    else:
        print("Congrats! you guessed it! the number was: ", number)
        break