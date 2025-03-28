#Enter the items in the list one by one and then show the list
def add_to_list():
    lst =[]
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem:
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
        
    return lst

def main():
    lst = add_to_list()
    print("Final list is: ", lst)
if __name__ == '__main__':
    main()