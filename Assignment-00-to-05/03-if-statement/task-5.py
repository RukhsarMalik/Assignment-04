#print 10 random numbers between 1 and 100
import random

def main():
   for i in range(10):
    print(random.randint(1,100))

if __name__ == '__main__':
    main()