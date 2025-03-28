TALL_HEIGHT = 4
height = float(input("Enter your height: "))

while height < TALL_HEIGHT:
    print("You're not tall enough to ride, but maybe next year!")
    height = float(input("Enter your height: "))
    if height >= TALL_HEIGHT:
        print("You're tall enough to ride!")
        break