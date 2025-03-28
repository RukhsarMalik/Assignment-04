#Converts feet to inches.

def feet_to_inches():
    feet = float(input("Enter the feet:"))
    inches = feet * 12
    print(str(feet) + " feet is equal to " + str(inches) + " inches.")
feet_to_inches()