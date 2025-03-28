C: int = 299792458

def speed_of_light():
    mass: int = float(input("Enter the mass of an object in kg: "))
    energy: int = mass * C**2
    print("e = mc^2")
    print("m = " + str(mass) + " kg")
    print("c = " + str(C) + " m/s")
    print("e = " + str(energy) + " J")

speed_of_light()