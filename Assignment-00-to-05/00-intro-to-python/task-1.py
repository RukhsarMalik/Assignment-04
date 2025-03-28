def add_two_numbers():
    num1 : str = input("Enter first number: ")
    num1 = int(num1)
    num2 : str = input("Enter second number: ")
    num2 = int(num2)
    total_sum = num1 + num2
    print(f"Sum of {num1} and {num2} is {total_sum}")

add_two_numbers()