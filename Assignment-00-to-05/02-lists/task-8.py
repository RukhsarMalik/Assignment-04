#Shorten list to the max-length and show the elements which we have removed to make it shorten

max_length : int = 3

def shorten_list(lst):
    while len(lst) > max_length:
        print("Removing element: ", lst.pop())
    return lst

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten_list(lst)
    print("Shortened list is: ", lst)


if __name__ == '__main__':
    main()