#Division with remainder

def remainder():
    a = int(input("Enter the interger you want to divide: "))
    b = int (input("Enter the interger you want to divide by: "))
    remainder = a % b
    result = a//b
    print(f"The result of this division is {result} with a remainder of {remainder}")

remainder()