def fer_to_cel():
    farenheit = float(input("Enter your temperature in Farenheit: "))
    degree_celcius = (farenheit - 32) * 5.0/9.0
    print(f"{farenheit} Farenheit is equal to {degree_celcius} Celcius")
fer_to_cel()