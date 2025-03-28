def roll_dice():
    import random
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    total: int = die1 + die2
    print(f"Dice_1 = {die1}, Dice_2 = {die2} and Total of two dices are: {total}")

def main():
    roll_dice()
    roll_dice()
    roll_dice()
    
if __name__ == '__main__':
    main()