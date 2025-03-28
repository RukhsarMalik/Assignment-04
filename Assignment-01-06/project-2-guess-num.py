import random
random_number = random.randint(1, 100)

def random_number_guess():
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print("You got it! The number was", random_number)

random_number_guess()