#Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    fruits = {"apple": 1.00, "banana": 1.50, "orange": 1.25, "mango": 2.00, "grape": 1.75, "kiwi": 1.50}
    total_cost = 0
    for fruit in fruits:
        num = int(input(f"How many {fruit}s do you want to buy? "))
        total_cost += num * fruits[fruit]
    print(f"The total cost of your fruits is ${total_cost:.2f}")

if __name__ == "__main__":
    main()