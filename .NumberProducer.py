import sys
from termcolor import colored
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Number Producer

@author Ryan Thompson

Prints out desired amount of numbers,
in either integer or float format.

python NumberProducer.py <i||f> <n> <base(float only)>
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Setting some constants
COLOR = "green"
COLOR_INT = "cyan"
COLOR_FLOAT = COLOR_INT # Got tired of picking different colors
COLOR_ENDS = "grey"

# Ask for integers or floats.
def getOption():
    print(colored("Pick integers<i>, floats<f>, or letter<l> ", COLOR, attrs=["bold"]),end="")
    choice = input()
    return choice

# Checking for cmd arguments.
# If no cmd args are provided, proceed
# to asking for args via terminal.
def argsCheck(firstList):
    tmp = []
    totalArgs = len(sys.argv)
    if(totalArgs > 1 and firstList == True):
        tmp.append(sys.argv[1]) # int or float
        tmp.append(sys.argv[2]) # amount of numbers
        if(totalArgs > 3):
            tmp.append(sys.argv[3]) # base value for floats
    else:
        decision = getOption()
        tmp.append(decision)
    return tmp

# Base of numbers. x.y
# Base = x
# ex) x=15 --> 15.y
def getBase():
    print(colored("Enter base value: ", COLOR, attrs=["bold"]), end="")
    retVal = input()
    return retVal

# Set & get amount of numbers
def getAmount():
    print(colored("Enter amount needed: ", COLOR, attrs=["bold"]), end="")
    n = input()
    return n

# Print integers
def intPrinter(n):
    for i in range(n):
        print(colored(str(i+1) + ")", COLOR_INT, attrs=["bold"]))

# Print floats
def floatPrinter(baseVal, n):
    for i in range(n):
        print(colored(str(baseVal) + "." + str(i+1) + ")", COLOR_FLOAT, attrs=["bold"]))

# Print letter-list
# Starts at the charater a
def letterPrinter():
    a = 97
    print(colored("\n<Letter-list starts at 'a'>", "green"))
    print(colored("Enter final letter: ", COLOR, attrs=["bold"]), end="")
    finalLetter = input()[0].lower()
    n = ord(finalLetter) - a +1
    for i in range(n):
        print(colored(str(chr((a+i))) + ")", COLOR_INT, attrs=["bold"]))

# Final setup for integers or floats
def makeFire(firstRound):
    exit = False
    args = argsCheck(firstRound)
    numArgs = len(args)
    n = 0
    decision = args[0] # Getting choice of int or float
    base = 0

    # Runnning cmd args
    if(numArgs > 1):
        #decision = args[0]
        n = args[1]
        n = int(n)
        if(numArgs == 3 and decision == "f"):
            base = args[2]
            floatPrinter(base, n)
        else:
            intPrinter(n)

    # Getting args via terminal.
    elif(numArgs <= 1):
        #decision = args[0]
        if(decision == 'n'):
            exit = True
            return exit
        elif(decision == "l"):
            letterPrinter()
        else:
            n = getAmount()

        n = int(n)
        # Going the float route.
        if(decision == "f"):
            base = getBase()
            floatPrinter(base, n)
        # Going the integer route
        if(decision == "i"):
            intPrinter(n)
        # if(decision == "n"):
        #     exit = True
    return exit



# Singals the start and end of this program,
# inside of the terminal.
def printLimit(point):
    print(colored("\n-----------------------------------------------------", COLOR_ENDS, attrs=["bold"]))
    print(colored("NumberProducer.py " + str(point), COLOR_ENDS, attrs=["bold"]))
    print(colored("-----------------------------------------------------\n", COLOR_ENDS, attrs=["bold"]))


# Driver function
def main():
    print() # Buffer white-space in terminal
    printLimit("START") # Opening
    stop = False
    roundOne = True

    # Keeps producing number-lists until stop == true.
    while(stop == False):
        stop = makeFire(roundOne)
        roundOne = False
        if(stop == False):
            print(colored("Would you like another list of numbers? <y/n> ",COLOR, attrs=["bold"]), end="")
        else:
            continue
        pick = input().lower()
        print()
        if(pick == "n" or pick == "no"): # Make it stop
            stop = True

    printLimit("END")  # Closing
    print() # Buffer white-space in terminal

# The big red button
main()