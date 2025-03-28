#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        numbers.append(num)
    return numbers

def count_numbers(num_lst):
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_count(num_dict):
    for num in num_dict:
        print(f"{num} occurs {num_dict[num]} times")

def main():
    numbers = get_numbers()
    num_dict = count_numbers(numbers)
    print_count(num_dict)

if __name__ == "__main__":
    main()