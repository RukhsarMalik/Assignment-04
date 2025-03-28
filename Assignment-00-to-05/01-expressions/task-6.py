#rolling two dice

def roll_dice():
    import random
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    result = dice_1 + dice_2
    print(f"Dice_1 = {dice_1}, Dice_2 = {dice_2} and Total of two dices are: {result}")

roll_dice()