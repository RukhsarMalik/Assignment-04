#Pythagorean theorem!
import math

def pythagorean_theorem():
    a = int(input("Enter the value of side AB: "))
    b = int(input("Enter the value of side AC: "))
    c: float = math.sqrt(a**2 + b**2)
    print("The value of c is: ", c)

pythagorean_theorem()