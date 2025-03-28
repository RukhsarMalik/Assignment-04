#Keep the track of phone numbers in a dictionary. The key will be the name and the value will be the phone number.

def get_numbers():
    numbers = {}
    while True:
        user_input = input("Enter a name: ")
        if user_input == "":
            break
        num = input("Enter a phone number: ")
        numbers[user_input] = num
    return numbers
def print_count(num_dict):
    for num in num_dict:
        print(f"{num} has the phone number {num_dict[num]}")

def lookup(num_dict):
    name = input("Enter a name to look up: ")
    if name in num_dict:
        print(f"{name} has the phone number {num_dict[name]}")
    else:
        print(f"{name} is not in the phone book")

def main():
    numbers = get_numbers()
    print_count(numbers)
    lookup(numbers)

if __name__ == "__main__":
    main()