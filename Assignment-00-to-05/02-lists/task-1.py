def add_many_numbers(numbers)->int:
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

def main():
    numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
    print(add_many_numbers(numbers))
if __name__ == '__main__':
    main()
  
