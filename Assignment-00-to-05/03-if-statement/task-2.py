PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age = int(input("Enter your age: "))
    if user_age >= PETURKSBOUIPO_AGE and user_age < STANLAU_AGE:
        print ("You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau and Mayengua where the voting ages are 25 and 48.")
    elif user_age >= STANLAU_AGE and user_age < MAYENGUA_AGE:
        print ("You can vote in Peturksbouipo and Stanlau where the voting ages are 16 and 25. You cannot vote in Mayengua where the voting age is 48.") 
    elif user_age >= MAYENGUA_AGE:
        print ("You can vote in Peturksbouipo ,Stanlau and Mayengua where the voting ages are 16, 25 and 48.")
    else:
        print("You Cannot Vote in Any Country")


if __name__ == '__main__':
    main()