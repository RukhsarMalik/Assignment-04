#double each element in the list
def double_list(lst):
    return [i*2 for i in lst]
def main():
    lst = [1, 2, 3, 4, 5,6,7,8,9,10]
    print(double_list(lst))
if __name__ == '__main__':
    main()