import sys
# import random
from termcolor import colored

#Set the upper limit
def set_target():
    n = 0
    length = len(sys.argv)
    if(length == 2):
        n = int(sys.argv[1])
    else:
        n = 9
    return n

#Produce the fibonacci sequence
def fibonacci(n):
    arr = [0, 1]
    i = 0
    while(i < n):
        clr = "pink"
        if(i%2 == 0):
            clr = "red"
        else:
            clr = "cyan"
        print(colored(str(arr[0]) + " ", clr))
        tmp = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = tmp
        i = i+1
    print()

#Driver function
def main():
    n = set_target()
    fibonacci(n)

#The big red button
main()