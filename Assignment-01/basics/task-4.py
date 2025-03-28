#Guess my number
import random
random_number = random.randint(0, 99)

print("I'm thinking of a number between 0 and 99...")
user_input = int(input("Enter a guess: "))

while True:
    if user_input > random_number:
        print("Too high!")
        user_input = int(input("Enter a guess: "))
    elif user_input < random_number:
        print("Too low!")
        user_input = int(input("Enter a guess: "))
    else:
        print("Congratulations! The number was:", random_number)
        break