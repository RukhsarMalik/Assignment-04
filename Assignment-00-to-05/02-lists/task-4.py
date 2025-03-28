#Enter the copy to the list

def add_three_copies():
    data = input("Enter a message you want to copy: ")
    lst = []
    print("List before adding the message: ", lst)
    for i in range(3):
        lst.append(data)
    print("List after adding the message: ", lst)
add_three_copies()