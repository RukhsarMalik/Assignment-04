# Get list as one element at one time and than show the last element of the list

def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
def last_element(lst):
    if len(lst) > 0:
        return lst[-1]
    else:
        return "List is empty"
def main():
    lst = get_lst()
    print("Last element of the list is: ", last_element(lst))
if __name__ == '__main__':
    main()
