from os import system, name

def clear():
    # Windows option
    if name == 'nt':
        system('cls')
    # Posix option
    else:
        system('clear')

def main():
    end = False
    while end == False:
        x = input("Clear the terminal(y/n)?(q to quit) ")
        # Clear the terminal.
        if x == "y":
            clear()
        # Quit
        elif x == "q":
            end = True
        # Don't clear the terminal
        else:
            print("Not clearing the terminal")

if __name__ == "__main__":
    main()