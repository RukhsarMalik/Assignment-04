my_sent = "I am capable of doing anything I put my mind to."
print("Please write this affermation:" + my_sent)

user_input = input("Please write the affermation: ")
while user_input != my_sent:
    print("That was not the affermation Please try again.")
    print("Please write this affermation:" + my_sent)

    user_input = input("Please write the affermation: ")
print("That is correct!")

